"""6.4.129–6.4.148 *bhādhikāra* slice: 6.4.130 / 134 / 146 / 148 with *bha*."""
from __future__ import annotations

import sutras  # noqa: F401

from engine            import apply_rule
from engine.state      import State, Term
from phonology         import mk


def _state_with_adhikaras(terms: list[Term]) -> State:
    s = State(terms=terms)
    s.adhikara_stack.append({
        "id": "6.4.1", "scope_end": "7.4.97", "text_dev": "अङ्गस्य",
    })
    s.adhikara_stack.append({
        "id": "6.4.129", "scope_end": "6.4.175", "text_dev": "भस्य",
    })
    return s


def test_6_4_134_upadha_a_before_n():
    anga = Term(
        kind="prakriti",
        varnas=[mk("r"), mk("A"), mk("j"), mk("a"), mk("n")],
        tags={"prātipadika", "anga", "pulliṅga", "bha"},
        meta={},
    )
    pr = Term(
        kind="pratyaya",
        varnas=[mk("a"), mk("s")],
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "Sas"},
    )
    s0 = _state_with_adhikaras([anga, pr])
    s1 = apply_rule("6.4.134", s0)
    assert "".join(v.slp1 for v in s1.terms[0].varnas) == "rAjn"


def test_6_4_130_pAda_to_pada():
    anga = Term(
        kind="prakriti",
        varnas=[mk("s"), mk("u"), mk("p"), mk("A"), mk("d")],
        tags={"prātipadika", "anga", "pulliṅga", "bha"},
        meta={},
    )
    pr = Term(
        kind="pratyaya",
        varnas=[mk("w"), mk("A")],
        tags={"sup", "pratyaya", "upadesha"},
        meta={"upadesha_slp1": "wA"},
    )
    s0 = _state_with_adhikaras([anga, pr])
    s1 = apply_rule("6.4.130", s0)
    assert "".join(v.slp1 for v in s1.terms[0].varnas) == "supad"


def test_6_4_146_o_to_guRa_anchor_before_y():
    anga = Term(
        kind="prakriti",
        varnas=[mk("m"), mk("A"), mk("d"), mk("h"), mk("o")],
        tags={"prātipadika", "anga", "pulliṅga", "bha"},
        meta={},
    )
    pr = Term(
        kind="pratyaya",
        varnas=[mk("y"), mk("a")],
        tags={"pratyaya", "upadesha"},
        meta={"upadesha_slp1": "yaw_test"},
    )
    s0 = _state_with_adhikaras([anga, pr])
    s1 = apply_rule("6.4.146", s0)
    assert s1.terms[0].varnas[-1].slp1 == "a"
