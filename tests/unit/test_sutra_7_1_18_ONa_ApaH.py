"""7.1.18 औङ आपः — औङ् (au / auṭ) after an āp-anta aṅga → शी.
Expectations: Kāśikā 7.1.18 udāharaṇa (खट्वे तिष्ठतः / खट्वे पश्य) and the vendored rādhā paradigm."""
from types import SimpleNamespace

import pytest

import sutras  # noqa: F401
from engine import apply_rule
from tools.autonomy_report import run_autonomously, start_state


def _run(stem, vib, linga):
    case = SimpleNamespace(kind="subanta", args=(stem, vib, 2, linga))
    return start_state(case), case


@pytest.mark.parametrize("stem,vib,gold", [
    ("KawvA", 1, "Kawve"), ("rADA", 1, "rADe"), ("KawvA", 2, "Kawve"), ("rADA", 2, "rADe"),
])
def test_au_becomes_SI_after_ap_and_derives_autonomously(stem, vib, gold):
    s, case = _run(stem, vib, "strīliṅga")
    after = apply_rule("7.1.18", s.clone())
    assert after.flat_slp1().endswith("SI")
    assert run_autonomously(s, gold, case.args[0], budget=80).outcome == "reached"


@pytest.mark.parametrize("stem,linga", [("rAma", "puṃliṅga"), ("nadI", "strīliṅga")])
def test_not_after_non_ap_stems(stem, linga):
    s, _ = _run(stem, 1, linga)
    assert apply_rule("7.1.18", s.clone()).flat_slp1() == s.flat_slp1()


def test_not_for_other_sups():
    from pipelines.subanta import build_initial_state, run_subanta_preflight_through_1_4_7

    s = build_initial_state("rADA", 3, 2, "strīliṅga")          # bhyām
    s = apply_rule("4.1.2", run_subanta_preflight_through_1_4_7(s))
    assert apply_rule("7.1.18", s.clone()).flat_slp1() == s.flat_slp1()
