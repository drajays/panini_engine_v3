from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from phonology.varna   import parse_slp1_upadesha_sequence


def _uttarapurva_ne_state(*, sarvanama: bool) -> State:
    tags = {"anga", "prātipadika", "diksamasa", "bahuvrihi"}
    if sarvanama:
        tags.add("sarvanama")
    anga = Term(
        kind="prakriti",
        varnas=[mk("u"), mk("t"), mk("t"), mk("a"), mk("r"), mk("a"),
                mk("p"), mk("U"), mk("r"), mk("v"), mk("A")],
        tags=tags,
        meta={"upadesha_slp1": "uttarapUrvA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ne"),
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Ne"},
    )
    return State(terms=[anga, pr])


def test_metadata():
    r = SUTRA_REGISTRY["7.3.113"]
    assert r.sutra_id == "7.3.113"
    assert r.sutra_type is SutraType.VIDHI


def test_yad_ap_non_sarvanama_ne():
    s0 = _uttarapurva_ne_state(sarvanama=False)
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.113", s0)
    assert s1.terms[0].varnas[-1].slp1 == "A"
    assert "".join(v.slp1 for v in s1.terms[1].varnas) == "yAe"
    assert s1.terms[1].meta.get("yad_ap_7_3_113_agama") == "yAw"


def test_no_fire_when_sarvanama():
    s0 = _uttarapurva_ne_state(sarvanama=True)
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.113", s0)
    assert s1.terms[1].meta.get("upadesha_slp1") == "Ne"


def test_uttarapurva_path_b_sandhi():
    s0 = _uttarapurva_ne_state(sarvanama=False)
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.113", s0)
    s2 = apply_rule("6.1.88", s1)
    assert s2.flat_slp1() == "uttarapUrvAyE"


def test_uttarapurva_path_a_sandhi():
    s0 = _uttarapurva_ne_state(sarvanama=True)
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    assert s1.terms[0].varnas[-1].slp1 == "a"
    assert "".join(v.slp1 for v in s1.terms[1].varnas) == "syAe"
    s2 = apply_rule("6.1.88", s1)
    assert s2.flat_slp1() == "uttarapUrvasyE"
