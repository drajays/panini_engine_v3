"""
7.2.117 *taddhiteṣu acām ādeḥ* — ādi-vṛddhi before ñit/ṇit taddhita.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY, apply_rule
from engine.sutra_type import SutraType
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _term_slp1(t: Term) -> str:
    return "".join(v.slp1 for v in t.varnas)


def _state(anga_slp1: str, *, it_markers: set[str]) -> State:
    anga = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(anga_slp1),
        tags={"anga"},
        meta={"upadesha_slp1": anga_slp1},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("iY"),  # shape irrelevant; markers are what matter here
        tags={"pratyaya", "taddhita"},
        meta={"upadesha_slp1": "iY", "it_markers": set(it_markers)},
    )
    s = State(terms=[anga, pr])
    s = apply_rule("6.4.1", s)  # open aṅgasya adhikāra
    return s


def test_registry():
    r = SUTRA_REGISTRY["7.2.117"]
    assert r.sutra_type is SutraType.VIDHI
    assert "taddhitezu" in r.text_slp1
    assert "अचामादेः" in r.text_dev
    assert "6.4.1" in r.anuvritti_from


def test_a_to_A_before_yit_taddhita():
    s0 = _state("dakza", it_markers={"Y"})  # ñit
    s1 = apply_rule("7.2.117", s0)
    assert _term_slp1(s1.terms[0]).startswith("dAk")  # dakza → dAkza


def test_I_to_E_before_yit_taddhita():
    s0 = _state("SIta", it_markers={"Y"})
    s1 = apply_rule("7.2.117", s0)
    assert _term_slp1(s1.terms[0]).startswith("SE")  # SI... → SE...


def test_u_to_O_before_nit_taddhita():
    s0 = _state("upagu", it_markers={"N"})  # ṇit-ish
    s1 = apply_rule("7.2.117", s0)
    assert _term_slp1(s1.terms[0]).startswith("Op")  # u... → O...


def test_o_to_O_before_yit_taddhita():
    s0 = _state("soma", it_markers={"Y"})
    s1 = apply_rule("7.2.117", s0)
    assert _term_slp1(s1.terms[0]).startswith("sO")  # so... → sO...


def test_requires_6_4_1_adhikara():
    anga = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("dakza"),
        tags={"anga"},
        meta={"upadesha_slp1": "dakza"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("iY"),
        tags={"pratyaya", "taddhita"},
        meta={"upadesha_slp1": "iY", "it_markers": {"Y"}},
    )
    s0 = State(terms=[anga, pr])
    s1 = apply_rule("7.2.117", s0)
    # Should be skipped (no adhikara): first vowel remains 'a'
    assert _term_slp1(s1.terms[0]).startswith("dak")

