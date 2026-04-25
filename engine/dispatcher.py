"""
engine/dispatcher.py — THE master apply_rule() router.
────────────────────────────────────────────────────────

Constitutional guarantees (CONSTITUTION.md Articles 1, 2, 3, 5):

  1. Fetch SutraRecord from registry.
  2. Purge closed adhikāras, then check gates:
       a. Asiddha gate (Tripāḍī firewall)
       b. Nipātana freeze
       c. Pratiṣedha block
       d. Vibhāṣā choice
  3. Route to exec_<type>() — dispatcher does NOT know what the rule does.
  4. Check R1/R2/R3 invariants.
  5. Append one TraceStep and return new state.

apply_rule is the ONLY public entry point for applying a sūtra.
Pipelines / recipes call it; exec_* functions do NOT call it
(no recursion through dispatcher — that is how v2 got into ordering loops).
"""
from __future__ import annotations

from typing import Any, Dict, Optional

from engine.gates      import (
    asiddha_violates,
    is_blocked,
    is_frozen_by_nipatana,
    purge_closed_adhikaras,
)
from engine.r1_check   import check_r1, check_r2, check_r3
from engine.registry   import get_sutra
from engine.state      import State
from engine.sutra_type import SutraRecord, SutraType, SUTRA_TYPE_CONTRACTS
from engine.telemetry  import notify_apply_rule_end
from engine.trace        import (
    META_1_3_9_VACUOUS,
    attach_chronological_transition,
    chronological_prev_sutra_id,
    make_applied_step,
    make_applied_vacuous_step,
    make_audit_step,
    make_skipped_step,
)


# Lazy import of executors to avoid circular imports at package load time.
def _executor_table():
    from engine.executors.exec_samjna      import exec_samjna
    from engine.executors.exec_paribhasha  import exec_paribhasha
    from engine.executors.exec_vidhi       import exec_vidhi
    from engine.executors.exec_niyama      import exec_niyama
    from engine.executors.exec_atidesha    import exec_atidesha
    from engine.executors.exec_adhikara    import exec_adhikara
    from engine.executors.exec_pratishedha import exec_pratishedha
    from engine.executors.exec_anuvada     import exec_anuvada
    from engine.executors.exec_vibhasha    import exec_vibhasha
    from engine.executors.exec_nipatana    import exec_nipatana
    return {
        SutraType.SAMJNA      : exec_samjna,
        SutraType.PARIBHASHA  : exec_paribhasha,
        SutraType.VIDHI       : exec_vidhi,
        SutraType.NIYAMA      : exec_niyama,
        SutraType.ATIDESHA    : exec_atidesha,
        SutraType.ADHIKARA    : exec_adhikara,
        SutraType.PRATISHEDHA : exec_pratishedha,
        SutraType.ANUVADA     : exec_anuvada,
        SutraType.VIBHASHA    : exec_vibhasha,
        SutraType.NIPATANA    : exec_nipatana,
    }


# Executor table cache (built on first call).
_EXEC_TABLE: Optional[Dict[SutraType, Any]] = None


def _append_traced_step(new_state: State, step: Dict[str, Any],
                        prev_sutra: Optional[str], current_sutra: str) -> None:
    new_state.trace.append(step)
    attach_chronological_transition(new_state.trace[-1], prev_sutra, current_sutra)


def _finish_apply_rule(
    prev_sutra: Optional[str], sutra_id: str, new_state: State,
) -> State:
    notify_apply_rule_end(prev_sutra, sutra_id, new_state)
    return new_state


def apply_rule(
    sutra_id    : str,
    state       : State,
    recipe_step : Optional[Dict[str, Any]] = None,
) -> State:
    """
    Apply one sūtra by id.  Returns a NEW state (state is not mutated).

    recipe_step may carry:
      "vibhasha_choice" : bool   — for VIBHASHA sūtras
      "target_term_idx" : int    — for exec_vidhi when ambiguous
      "note"            : str    — a scholarly remark attached to the step
    """
    global _EXEC_TABLE
    if _EXEC_TABLE is None:
        _EXEC_TABLE = _executor_table()

    recipe_step = recipe_step or {}
    rec         = get_sutra(sutra_id)
    stype       = rec.sutra_type
    contract    = SUTRA_TYPE_CONTRACTS[stype]
    # Chronological “edge into” this invocation (previous non-structural sūtra, if any).
    prev_sutra  = chronological_prev_sutra_id(state.trace)

    new_state   = state.clone()
    purge_closed_adhikaras(sutra_id, new_state)

    form_before   = new_state.render()
    samjna_before = dict(new_state.samjna_registry)
    parib_before  = dict(new_state.paribhasha_gates)

    # ── Gate 1: Tripāḍī asiddha firewall ─────────────────────────────
    if asiddha_violates(sutra_id, new_state):
        _append_traced_step(
            new_state,
            make_skipped_step(
                sutra_id, stype.name, contract["dev_label"], form_before,
                rec.why_dev, "ASIDDHA-GATE (cannot fire outside Tripāḍī once entered)",
            ),
            prev_sutra, sutra_id,
        )
        return _finish_apply_rule(prev_sutra, sutra_id, new_state)

    # ── Gate 2: Nipātana freeze ──────────────────────────────────────
    if is_frozen_by_nipatana(stype, new_state):
        _append_traced_step(
            new_state,
            make_skipped_step(
                sutra_id, stype.name, contract["dev_label"], form_before,
                rec.why_dev, "NIPATANA-FROZEN",
            ),
            prev_sutra, sutra_id,
        )
        return _finish_apply_rule(prev_sutra, sutra_id, new_state)

    # ── Gate 3: Pratiṣedha block ─────────────────────────────────────
    if is_blocked(sutra_id, new_state):
        _append_traced_step(
            new_state,
            make_skipped_step(
                sutra_id, stype.name, contract["dev_label"], form_before,
                rec.why_dev, "PRATISHEDHA-BLOCKED",
            ),
            prev_sutra, sutra_id,
        )
        return _finish_apply_rule(prev_sutra, sutra_id, new_state)

    # ── Gate 4: Vibhāṣā recipe choice ────────────────────────────────
    if stype is SutraType.VIBHASHA:
        choice = recipe_step.get("vibhasha_choice", rec.vibhasha_default)
        if not choice:
            new_state.vibhasha_forks.append({
                "sutra_id"    : sutra_id,
                "choice_made" : False,
                "alternative" : form_before,
            })
            _append_traced_step(
                new_state,
                make_skipped_step(
                    sutra_id, stype.name, contract["dev_label"], form_before,
                    rec.why_dev, "VIBHASHA-DECLINED",
                ),
                prev_sutra, sutra_id,
            )
            return _finish_apply_rule(prev_sutra, sutra_id, new_state)

    # ── Dispatch to executor (the ONLY place we call exec_*) ─────────
    exec_fn = _EXEC_TABLE[stype]
    try:
        new_state, fired = exec_fn(rec, new_state, recipe_step)
    except Exception as ex:
        # Do NOT swallow executor errors — bubble up with context.
        raise RuntimeError(
            f"executor for {sutra_id} ({stype.name}) raised: {ex}"
        ) from ex

    form_after = new_state.render()

    if not fired:
        _sd = getattr(rec, "skip_detail_cond_false", None)
        _append_traced_step(
            new_state,
            make_skipped_step(
                sutra_id, stype.name, contract["dev_label"], form_before,
                rec.why_dev, "COND-FALSE",
                skip_detail=_sd,
            ),
            prev_sutra, sutra_id,
        )
        return _finish_apply_rule(prev_sutra, sutra_id, new_state)

    # **1.3.9** — *it*-*prakaraṇa* *vidhi* is *paryālayit* even when there is no *it* to
    # *lop*; executor signals vacuous *prayoga* (not *COND-FALSE* *skip*).
    if new_state.meta.pop(META_1_3_9_VACUOUS, None):
        w_v = getattr(rec, "why_dev_vacuous", None) or rec.why_dev
        _append_traced_step(
            new_state,
            make_applied_vacuous_step(
                sutra_id, stype.name, contract["dev_label"],
                form_before, form_after, w_v, lopa_count=0,
            ),
            prev_sutra, sutra_id,
        )
        return _finish_apply_rule(prev_sutra, sutra_id, new_state)

    # ── Invariant checks on APPLIED step ─────────────────────────────
    check_r1(rec, form_before, form_after)
    check_r2(rec, samjna_before, new_state.samjna_registry)
    check_r3(rec, parib_before,  new_state.paribhasha_gates)

    # *अधिकार* / *paribhāṣā* / *anuvāda* — *prayoga* without surface *pariṇāma*:
    # trace as AUDIT, not *vidhi* *APPLIED* (UI / analytics).
    if stype in (SutraType.ADHIKARA, SutraType.PARIBHASHA, SutraType.ANUVADA):
        _append_traced_step(
            new_state,
            make_audit_step(
                sutra_id, stype.name, contract["dev_label"],
                form_before, form_after, rec.why_dev,
            ),
            prev_sutra, sutra_id,
        )
    else:
        _append_traced_step(
            new_state,
            make_applied_step(
                sutra_id, stype.name, contract["dev_label"],
                form_before, form_after, rec.why_dev,
            ),
            prev_sutra, sutra_id,
        )
    return _finish_apply_rule(prev_sutra, sutra_id, new_state)
