"""
tests/unit/test_dispatcher_r1.py
──────────────────────────────────

R1 invariant: a non-exempt form-mutating sūtra that reports 'fired'
MUST have changed state.render() — else the dispatcher raises
R1Violation.

We build a synthetic VIDHI sūtra whose cond returns True and whose
act returns the state unchanged, register it, and assert the
dispatcher raises.
"""
from __future__ import annotations

import pytest

from engine            import SutraType, SutraRecord, register_sutra, apply_rule
from engine.r1_check   import R1Violation
from engine.state      import State, Term
from phonology         import mk


def _build_noop_vidhi():
    def cond(state): return True
    def act(state):  return state  # DOES NOTHING — should trigger R1

    rec = SutraRecord(
        sutra_id       = "1.1.99",
        sutra_type     = SutraType.VIDHI,
        text_slp1      = "testNoopVidhi",
        text_dev       = "परीक्षा-अविकारि-विधि",
        padaccheda_dev = "परीक्षा अविकारि विधिः",
        why_dev        = "R1 परीक्षणम्।",
        cond           = cond,
        act            = act,
    )
    # Allow silent re-registration if test is re-run.
    from engine.registry import SUTRA_REGISTRY
    SUTRA_REGISTRY.pop("1.1.99", None)
    register_sutra(rec)


def test_r1_fires_on_noop_vidhi():
    _build_noop_vidhi()
    s = State(terms=[Term(kind="prakriti", varnas=[mk("k"), mk("a")])])
    with pytest.raises(R1Violation):
        apply_rule("1.1.99", s)
