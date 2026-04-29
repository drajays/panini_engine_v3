"""``flat_slp1()`` keeps *it* letters on the tape until **1.3.9** (not at 1.3.2–8)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.lopa_ghost import LUK_LOPA_GHOST_TAG
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def test_luk_lopa_ghost_term_contributes_no_phonetic_slp1_even_if_varnas_nonempty():
    """Defense-in-depth: **2.4.71** ghosts must not leak into ``flat_slp1()``."""
    ghost = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("X")),
        tags={"sup", "pratyaya", LUK_LOPA_GHOST_TAG},
        meta={},
    )
    s = State(terms=[ghost])
    assert s.flat_slp1() == ""


def test_Ne_itarjanam_flat_keeps_N_until_1_3_9_lopa():
    anga = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("uttarapUrvA")),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "uttarapUrvA"},
    )
    pr = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("Ne"),
        tags={"sup", "upadesha", "pratyaya", "has_initial_n_it"},
        meta={"upadesha_slp1": "Ne"},
    )
    s = State(terms=[anga, pr])
    assert s.flat_slp1() == "uttarapUrvANe"
    for rid in ("1.3.2", "1.3.3", "1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8"):
        s = apply_rule(rid, s)
    # *N* is still a Varṇa; **1.3.3** is *saṃjñā* only; **1.3.9** is *lopa* *vidhi*.
    assert s.flat_slp1() == "uttarapUrvANe", s.flat_slp1()
    assert any("it_candidate_lasaku" in v.tags for v in s.terms[1].varnas)
    s = apply_rule("1.3.9", s)
    assert s.flat_slp1() == "uttarapUrvAe"
    assert s.terms[1].meta.get("it_markers") == {"N"}, s.terms[1].meta.get("it_markers")


def test_1_3_3_samjna_unchanged_flat_1_3_9_drops_T_jayati_laT():
    """*Halantyam* (1.3.3) tags only; *lopa* (1.3.9) removes the ``T`` row (Issue 1)."""
    from tools.tinanta_jayati_gold import run_jayati_gold_step2

    s = run_jayati_gold_step2()
    assert s.flat_slp1() == "jilaT"
    flat_before_13_3 = s.flat_slp1()
    s = apply_rule("1.3.3", s)
    assert s.flat_slp1() == flat_before_13_3
    for rid in ("1.3.4", "1.3.5", "1.3.6", "1.3.7", "1.3.8"):
        s = apply_rule(rid, s)
    assert s.flat_slp1() == "jilaT", s.flat_slp1()
    s = apply_rule("1.3.9", s)
    assert s.flat_slp1() == "jila"
    assert "T" not in s.flat_slp1()
