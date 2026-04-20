"""
engine/trace.py — TraceStep schema and trace helpers.
──────────────────────────────────────────────────────

Schema (v3.1):
    sutra_id / sutra_type / type_label / form_before / form_after /
    why_dev / status ∈ {APPLIED, SKIPPED, BLOCKED}
    gate_reason  : present when status == "BLOCKED"
    skip_reason  : present when status == "SKIPPED"

v3.1 amendment — BLOCKED vs SKIPPED:
    BLOCKED : explicit gate forbade the sūtra (pratiṣedha,
              nipātana-freeze, tripāḍī-asiddha, vibhāṣā-declined).
    SKIPPED : cond() ran and returned False (no trigger).
"""
from __future__ import annotations

from typing import Any, Dict


TRACE_STATUS_APPLIED = "APPLIED"
TRACE_STATUS_SKIPPED = "SKIPPED"
TRACE_STATUS_BLOCKED = "BLOCKED"

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


def make_skipped_step(sutra_id, sutra_type, type_label,
                      form_before, why_dev, reason):
    """
    Back-compat helper for v3.0 callers.  If `reason` is a GATE_* token,
    we upgrade to BLOCKED (v3.1 distinction).  Otherwise this is a
    generic SKIPPED row carrying `reason` as skip_reason.
    """
    if reason in _GATE_REASONS:
        return make_blocked_step(
            sutra_id, sutra_type, type_label, form_before, why_dev, reason,
        )
    return {
        "sutra_id"    : sutra_id,
        "sutra_type"  : sutra_type,
        "type_label"  : type_label,
        "form_before" : form_before,
        "form_after"  : form_before,
        "why_dev"     : why_dev,
        "status"      : TRACE_STATUS_SKIPPED,
        "skip_reason" : reason,
    }
