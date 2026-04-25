from __future__ import annotations

import sutras  # noqa: F401

from engine            import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state      import State, Term
from phonology         import mk
from phonology.varna   import parse_slp1_upadesha_sequence


def _kA_ne_state() -> State:
    anga = Term(
        kind="prakriti",
        varnas=[mk("k"), mk("A")],
        tags={"anga", "prātipadika", "sarvanama"},
        meta={"upadesha_slp1": "kA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ne"),
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Ne"},
    )
    return State(terms=[anga, pr])


def test_metadata():
    r = SUTRA_REGISTRY["7.3.114"]
    assert r.sutra_id == "7.3.114"
    assert r.sutra_type is SutraType.VIDHI


def test_hrasva_and_syat_under_6_4_1():
    s0 = _kA_ne_state()
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    assert s1.terms[0].varnas[-1].slp1 == "a"
    assert "".join(v.slp1 for v in s1.terms[1].varnas) == "syAe"
    assert s1.terms[1].meta.get("syat_7_3_114_agama") == "syAw"
    assert s1.terms[1].meta.get("syat_7_3_114_done") is True


def test_no_fire_without_sarvanama():
    anga = Term(
        kind="prakriti",
        varnas=[mk("k"), mk("A")],
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "kA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ne"),
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Ne"},
    )
    s0 = State(terms=[anga, pr])
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    assert s1.terms[0].varnas[-1].slp1 == "A"


def test_no_fire_for_ghi_stem():
    anga = Term(
        kind="prakriti",
        varnas=[mk("h"), mk("a"), mk("r"), mk("i")],
        tags={"anga", "prātipadika", "sarvanama", "ghi"},
        meta={"upadesha_slp1": "hari"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ne"),
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Ne"},
    )
    s0 = State(terms=[anga, pr])
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    assert s1.terms[0].varnas[-1].slp1 == "i"


def test_vrddhi_after_7_3_114_chain():
    s0 = _kA_ne_state()
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    s2 = apply_rule("6.1.88", s1)
    assert s2.flat_slp1() == "kasyE"


def _kA_ngit_state(up: str) -> State:
    anga = Term(
        kind="prakriti",
        varnas=[mk("k"), mk("A")],
        tags={"anga", "prātipadika", "sarvanama"},
        meta={"upadesha_slp1": "kA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence(up),
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": up},
    )
    return State(terms=[anga, pr])


def test_nas_remainder_and_dirgha_chain():
    s0 = _kA_ngit_state("Nas")
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    assert s1.terms[0].varnas[-1].slp1 == "a"
    assert "".join(v.slp1 for v in s1.terms[1].varnas) == "as"
    assert s1.terms[1].meta.get("upadesha_slp1") == "as"
    s2 = apply_rule("6.1.101", s1)
    assert "A" in s2.flat_slp1()
    assert "s" in s2.flat_slp1()


def test_nasi_remainder():
    s0 = _kA_ngit_state("Nasi")
    s0 = apply_rule("6.4.1", s0)
    s1 = apply_rule("7.3.114", s0)
    assert "".join(v.slp1 for v in s1.terms[1].varnas) == "asi"
    assert s1.terms[1].meta.get("syat_7_3_114_agama") == "syAw"


def test_7_1_14_does_not_fire_on_A_final_sarvanama():
    """7.1.14 is *adanta*; **kā** + **Ne** must stay **Ne** for 7.3.114."""
    anga = Term(
        kind="prakriti",
        varnas=[mk("k"), mk("A")],
        tags={"anga", "prātipadika", "sarvanama"},
        meta={"upadesha_slp1": "kA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ne"),
        tags={"sup", "upadesha", "pratyaya"},
        meta={"upadesha_slp1": "Ne"},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("7.1.14", s0)
    assert s1.terms[1].meta.get("upadesha_slp1") == "Ne"
