"""
engine/trace.py — TraceStep schema and trace helpers.
──────────────────────────────────────────────────────

Schema (v3.1):
    sutra_id / sutra_type / type_label / form_before / form_after /
    why_dev / status ∈ {APPLIED, SKIPPED, BLOCKED}
    gate_reason  : present when status == "BLOCKED"
    skip_reason  : present when status == "SKIPPED"
    skip_detail  : optional, human *śāstrīya* gloss for *COND-FALSE* (sūtra file)
    lopa_count   : optional, when status == "APPLIED_VACUOUS" (1.3.9 *śūnya* *lopa*)

Optional (tools / gold *prakriyā* display only, not read by ``cond``):
    it_tagged_this_step : list of affix.letter labels for *it* *saṃjñā* *śūnya* steps
    adhikara_range / vidhi_aspect : *adhikāra* pedagogy (e.g. *jayati* step 2)
    chronological_transition : { from_sutra, to_sutra } on every row from ``apply_rule``
        (``from_sutra`` is *null* on the first sūtra in a derivation; **SIG** / Markov
        use the full sequence).

v3.1 amendment — BLOCKED vs SKIPPED:
    BLOCKED : explicit gate forbade the sūtra (pratiṣedha,
              nipātana-freeze, tripāḍī-asiddha, vibhāṣā-declined).
    SKIPPED : cond() ran and returned False (no trigger).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


TRACE_STATUS_APPLIED = "APPLIED"
TRACE_STATUS_APPLIED_VACUOUS = "APPLIED_VACUOUS"
TRACE_STATUS_SKIPPED = "SKIPPED"
TRACE_STATUS_BLOCKED = "BLOCKED"

# Dispatcher-only: *vidhi* ran (cond satisfied vacuously) for **1.3.9** when there is
# no *it* row to *lop* — still a checked application, not **COND-FALSE** skip.
META_1_3_9_VACUOUS = "_engine_trace_1_3_9_vacuous"

# Gate-reason tokens — stable; tools/tests grep for them.
GATE_PRATISHEDHA    = "PRATISHEDHA-BLOCKED"
GATE_NIPATANA       = "NIPATANA-FROZEN"
GATE_ASIDDHA        = "ASIDDHA-GATE"
GATE_VIBHASHA       = "VIBHASHA-DECLINED"
GATE_WRONG_PHASE    = "WRONG-PHASE"
GATE_OUT_OF_ADHIK   = "OUT-OF-ADHIKARA"

SKIP_COND_FALSE     = "COND-FALSE"

_GATE_REASONS = frozenset({
    GATE_PRATISHEDHA, GATE_NIPATANA, GATE_ASIDDHA, GATE_VIBHASHA,
    GATE_WRONG_PHASE, GATE_OUT_OF_ADHIK,
})


class TraceStep(Dict[str, Any]):
    pass


def make_applied_step(sutra_id, sutra_type, type_label,
                      form_before, form_after, why_dev):
    return {
        "sutra_id"    : sutra_id,
        "sutra_type"  : sutra_type,
        "type_label"  : type_label,
        "form_before" : form_before,
        "form_after"  : form_after,
        "why_dev"     : why_dev,
        "status"      : TRACE_STATUS_APPLIED,
    }


def make_applied_vacuous_step(
    sutra_id, sutra_type, type_label,
    form_before, form_after, why_dev, *,
    lopa_count: int = 0,
):
    """*Vidhi* checked and applied with zero phonetic *pariṇāma* (e.g. **1.3.9** with no *it*)."""
    d: TraceStep = {
        "sutra_id"    : sutra_id,
        "sutra_type"  : sutra_type,
        "type_label"  : type_label,
        "form_before" : form_before,
        "form_after"  : form_after,
        "why_dev"     : why_dev,
        "status"      : TRACE_STATUS_APPLIED_VACUOUS,
        "lopa_count"  : lopa_count,
    }
    return d


def make_blocked_step(sutra_id, sutra_type, type_label,
                      form_before, why_dev, gate_reason):
    return {
        "sutra_id"    : sutra_id,
        "sutra_type"  : sutra_type,
        "type_label"  : type_label,
        "form_before" : form_before,
        "form_after"  : form_before,
        "why_dev"     : why_dev,
        "status"      : TRACE_STATUS_BLOCKED,
        "gate_reason" : gate_reason,
    }


def make_cond_false_step(sutra_id, sutra_type, type_label,
                         form_before, why_dev):
    return {
        "sutra_id"    : sutra_id,
        "sutra_type"  : sutra_type,
        "type_label"  : type_label,
        "form_before" : form_before,
        "form_after"  : form_before,
        "why_dev"     : why_dev,
        "status"      : TRACE_STATUS_SKIPPED,
        "skip_reason" : SKIP_COND_FALSE,
    }


def make_skipped_step(
    sutra_id, sutra_type, type_label,
    form_before, why_dev, reason, *,
    skip_detail: str | None = None,
):
    """
    Back-compat helper for v3.0 callers.  If `reason` is a GATE_* token,
    we upgrade to BLOCKED (v3.1 distinction).  Otherwise this is a
    generic SKIPPED row carrying `reason` as skip_reason.
    `skip_detail` (optional) elaborates *COND-FALSE* for *śāstrīya* UIs.
    """
    if reason in _GATE_REASONS:
        return make_blocked_step(
            sutra_id, sutra_type, type_label, form_before, why_dev, reason,
        )
    d: TraceStep = {
        "sutra_id"    : sutra_id,
        "sutra_type"  : sutra_type,
        "type_label"  : type_label,
        "form_before" : form_before,
        "form_after"  : form_before,
        "why_dev"     : why_dev,
        "status"      : TRACE_STATUS_SKIPPED,
        "skip_reason" : reason,
    }
    if skip_detail:
        d["skip_detail"] = skip_detail
    return d


# ── Chronological global journey (one row per apply_rule) ─────────────

def extract_chronological_sutra_sequence(trace: List[Dict[str, Any]]) -> List[str]:
    """All registered sūtra_ids in **invocation order** (excludes ``__*__``)."""
    out: List[str] = []
    for step in trace:
        sid = step.get("sutra_id", "")
        if not sid or sid.startswith("__"):
            continue
        out.append(sid)
    return out


def chronological_prev_sutra_id(trace: List[Dict[str, Any]]) -> Optional[str]:
    """Last non-structural sūtra on ``trace`` before the next ``apply_rule`` call."""
    seq = extract_chronological_sutra_sequence(trace)
    return seq[-1] if seq else None


def attach_chronological_transition(
    step: Dict[str, Any],
    from_sutra: Optional[str],
    to_sutra: str,
) -> None:
    step["chronological_transition"] = {
        "from_sutra": from_sutra,
        "to_sutra"  : to_sutra,
    }
