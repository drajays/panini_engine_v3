"""
engine/fixed_point.py — Bounded aṅgakārya convergence sweep.
──────────────────────────────────────────────────────────────

CONSTITUTION v3.1 amendment — Article 7.3 promoted from DEFERRED.

Why this exists: Adhyāya 6.4.x / 7.x aṅgakārya rules form a network
where applying rule A can create the trigger for rule B (e.g.
6.4.148 yasyeti-ca lopa enables 7.3.102 supi ca guṇa which then
requires 6.4.148 to re-check).  A linear pass through the rule list
misses these cascades.

The sweep repeats the rule list until the flat SLP1 form no longer
changes, up to MAX_ANGAKARYA_SWEEPS iterations.  Hitting the bound
means either (a) a genuine oscillation bug in the rule set or (b)
a rule whose cond() is not idempotent — either way it is a fault and
we raise FixedPointError rather than silently truncate.

This module is purely an orchestration helper.  It does NOT bypass
apply_rule() — every step still goes through the dispatcher, so gates,
R1, trace, and SIG all continue to work normally.
"""
from __future__ import annotations

from typing import List

from engine.state import State


MAX_ANGAKARYA_SWEEPS = 10


class FixedPointError(RuntimeError):
    """Aṅgakārya sweep did not converge within MAX_ANGAKARYA_SWEEPS."""


def run_to_fixed_point(sutra_ids: List[str], state: State) -> State:
    """
    Apply `sutra_ids` in order, repeatedly, until the flat SLP1 form
    stops changing.  Each sūtra in the list goes through apply_rule()
    normally — gates, R1, and trace are preserved.

    Returns the converged state.  Raises FixedPointError if no
    convergence within MAX_ANGAKARYA_SWEEPS.
    """
    from engine.dispatcher import apply_rule  # local import: avoid cycle

    last_form = None
    for sweep_n in range(MAX_ANGAKARYA_SWEEPS):
        form_before_sweep = state.flat_slp1()
        for sid in sutra_ids:
            state = apply_rule(sid, state)
        form_after_sweep = state.flat_slp1()
        if form_before_sweep == form_after_sweep:
            # Converged.  Log as a structural trace note so audits can
            # see how many sweeps a derivation needed.
            state.trace.append({
                "sutra_id"    : "__FIXED_POINT__",
                "sutra_type"  : "STRUCTURAL",
                "type_label"  : "स्थिर-बिन्दु-सम्प्राप्तिः",
                "form_before" : form_after_sweep,
                "form_after"  : form_after_sweep,
                "why_dev"     : (
                    f"अङ्गकार्य-आवृत्तिषु {sweep_n + 1} सम्प्राप्तिः। "
                    f"(sutra_ids: {len(sutra_ids)})"
                ),
                "status"      : "APPLIED",
                "sweeps_run"  : sweep_n + 1,
            })
            return state
        last_form = form_after_sweep

    raise FixedPointError(
        f"aṅgakārya sweep did not converge in {MAX_ANGAKARYA_SWEEPS} passes; "
        f"last form: {last_form!r}; rules attempted: {sutra_ids!r}. "
        "Likely causes: (1) a VIDHI whose cond() is not idempotent and "
        "re-fires on its own output, (2) two rules that alternately "
        "undo each other, or (3) MAX_ANGAKARYA_SWEEPS is genuinely too "
        "low for this paradigm — raise it explicitly via a named "
        "amendment, do not silently patch."
    )
