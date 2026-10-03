"""Audit findings (2026-10-03) closed with tests: 7.1.35 is a real replacement with a UI trace;
3.4.99 and 8.4.56 decide on the tape (no gate-eligibility backdoor), explain themselves, and 8.4.56 is a vibhāṣā."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY
from engine.sutra_type import SutraType
from engine.vikalpa import choose
from pipelines.subanta import derive as sub
from pipelines.tinanta import derive as tin
from tools.autonomy_report import run_autonomously, start_state


def _step(state, sid):
    return [t for t in state.trace if t["sutra_id"] == sid]


def test_7_1_35_replaces_tu_with_tAt_and_explains_itself():
    case = NS(kind="tinanta", args=("BU", "loT", 3, 1), ashis=True)
    run = run_autonomously(start_state(case), "", "BU", 150)
    assert run.surface == "BavatAt"
    row = next(s for s in run.steps if s[0] == "7.1.35")
    assert row[1].endswith("tu") and row[2].endswith("tAta~N")      # the actual replacement, not a gate flip


def test_7_1_35_cond_looks_for_tu_or_hi():
    rec = SUTRA = SUTRA_REGISTRY["7.1.35"]
    assert rec.sutra_type is SutraType.VIBHASHA
    state = start_state(NS(kind="tinanta", args=("BU", "loT", 3, 3), ashis=True))   # tiṅ is jhi, not tu/hi
    assert not rec.cond(state)


def test_3_4_99_applies_only_where_there_is_an_s_to_drop_and_says_why():
    laG = tin("BU", "laG", "kartari", 1, 2)                 # vas → va
    rows = _step(laG, "3.4.99")
    assert rows and rows[-1]["status"] == "APPLIED" and rows[-1].get("why_now_dev")
    assert not [r for r in _step(tin("BU", "laT", "kartari", 1, 2), "3.4.99") if r["status"] == "APPLIED"]  # laṭ keeps vas


def test_3_4_99_cond_is_structural():
    import inspect
    from sutras.adhyaya_3.pada_4 import sutra_3_4_99 as m

    assert "gate_eligible" not in inspect.getsource(m)


def test_8_4_56_is_a_vibhasha_that_forks():
    assert SUTRA_REGISTRY["8.4.56"].sutra_type is SutraType.VIBHASHA
    with choose({"8.4.56": True}):
        assert sub("vAc", 1, 1, linga="strīliṅga").flat_slp1() == "vAk"
    with choose({"8.4.56": False}):
        assert sub("vAc", 1, 1, linga="strīliṅga").flat_slp1() == "vAg"      # the other valid reading


def test_8_4_56_traces_why():
    row = _step(sub("vAc", 1, 1, linga="strīliṅga"), "8.4.56")[-1]
    assert row["status"] == "APPLIED" and row.get("why_now_dev")


def test_8_4_56_cond_is_structural():
    import inspect
    from sutras.adhyaya_8.pada_4 import sutra_8_4_56 as m

    assert "gate_eligible" not in inspect.getsource(m)
