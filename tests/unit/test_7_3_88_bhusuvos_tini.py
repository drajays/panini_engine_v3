"""7.3.88 भूसुवोस्तिङि — the निषेध that keeps सू and भू without guṇa before a tiṅ.

Kāśikā: सुवै, सुवावहै, सुवामहै; अभूत्; pratyudāharaṇa भवति (śap intervenes).
"""
from __future__ import annotations

from types import SimpleNamespace as NS

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from tools.autonomy_report import run_autonomously, start_state


def _loop(ref, lakara, purusha, vacana):
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lakara, purusha, vacana), pada=None)), "", ref, 250)


def _status(trace, sutra_id):
    return [s.get("status") for s in trace if s.get("sutra_id") == sutra_id]


def test_is_a_pratishedha_of_7_3_84():
    rec = SUTRA_REGISTRY["7.3.88"]
    assert rec.sutra_type is SutraType.PRATISHEDHA
    assert rec.blocks_sutra_ids == ("7.3.84",)


def test_su_lot_uttama_blocks_guna():
    run = _loop("Adadi_02_0025", "loT", 1, 3)
    assert run.surface == "suvAmahE"
    assert "APPLIED" in _status(run.state.trace, "7.3.88")
    assert "7.3.84" in run.state.blocked_sutras


def test_guna_asked_where_it_would_apply_is_blocked():
    """Stop the loop at the step 7.3.88 fires (sū + āṭ + mahai on the tape) and ask for 7.3.84 there."""
    start = lambda: start_state(NS(kind="tinanta", args=("Adadi_02_0025", "loT", 1, 3), pada=None))
    for budget in range(1, 80):
        state = run_autonomously(start(), "", "su", budget).state
        if "APPLIED" in _status(state.trace, "7.3.88"):
            break
    before = state.flat_slp1()
    after = apply_rule("7.3.84", state)
    assert _status(after.trace, "7.3.84")[-1] == "BLOCKED"
    assert after.flat_slp1() == before


def test_bhu_lun_and_lat():
    assert _loop("BvAdi_01_0001", "luG", 3, 1).surface == "aBUt"
    lat = _loop("BvAdi_01_0001", "laT", 3, 1)
    assert lat.surface == "Bavati"                       # śap stands between: guṇa, no निषेध
    assert "APPLIED" not in _status(lat.state.trace, "7.3.88")
