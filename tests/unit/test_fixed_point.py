"""
tests/unit/test_fixed_point.py
────────────────────────────────

Tests for run_to_fixed_point / FixedPointError (v3.1 amendment).
"""
from __future__ import annotations

import pytest

from engine            import (
    run_to_fixed_point, FixedPointError, MAX_ANGAKARYA_SWEEPS,
    SutraType, SutraRecord, register_sutra, SUTRA_REGISTRY,
)
from engine.state      import State, Term
from phonology         import mk


def test_empty_rule_list_converges_trivially():
    s = State(terms=[Term(kind="prakriti", varnas=[mk("a")])])
    out = run_to_fixed_point([], s)
    # No rules ran — form unchanged; trace gets ONE __FIXED_POINT__ row.
    assert out.flat_slp1() == s.flat_slp1()
    assert any(r.get("sutra_id") == "__FIXED_POINT__" for r in out.trace)


def test_converges_with_single_pass():
    # All our existing 20 sūtras are idempotent — running them from an
    # empty state should converge in 1 sweep.
    s = State(terms=[Term(kind="prakriti", varnas=[mk("r"), mk("a")],
                          tags={"prātipadika", "anga", "upadesha"},
                          meta={"upadesha_slp1": "rA"})])
    out = run_to_fixed_point(["1.1.2"], s)
    # Look for the structural row recording sweeps_run.
    fp_rows = [r for r in out.trace if r.get("sutra_id") == "__FIXED_POINT__"]
    assert len(fp_rows) == 1
    assert fp_rows[0]["sweeps_run"] == 1


def test_non_converging_rule_raises_fixed_point_error():
    """
    A rule that changes the form on every sweep (never idempotent) must
    hit MAX_ANGAKARYA_SWEEPS and raise.  We simulate this with a VIDHI
    that appends an 'a' varṇa every time — its cond() stays True forever
    because there's always a position that lacks appendage.
    """
    SUTRA_REGISTRY.pop("0.0.1", None)

    counter = {"n": 0}

    def cond_always(state):
        # Fire up to 100 times — enough to blow past MAX_ANGAKARYA_SWEEPS.
        return counter["n"] < 100

    def act_append_a(state):
        counter["n"] += 1
        if state.terms:
            state.terms[-1].varnas.append(mk("a"))
        return state

    rec = SutraRecord(
        sutra_id="0.0.1", sutra_type=SutraType.VIDHI,
        text_slp1="appender", text_dev="परीक्षा-वृद्धिः",
        padaccheda_dev="परीक्षा",
        why_dev="परीक्षार्थं सर्वदा अ-वर्णं योजयति।",
        cond=cond_always, act=act_append_a,
    )
    register_sutra(rec)

    s = State(terms=[Term(kind="prakriti", varnas=[mk("k")])])
    with pytest.raises(FixedPointError):
        run_to_fixed_point(["0.0.1"], s)

    SUTRA_REGISTRY.pop("0.0.1", None)


def test_max_sweeps_is_exposed():
    assert MAX_ANGAKARYA_SWEEPS == 10
