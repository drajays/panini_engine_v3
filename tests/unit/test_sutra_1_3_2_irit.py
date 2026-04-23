"""1.3.2 irit (इँर्) vārttika — Varṇa-tag path + 1.3.9 drops i+r."""
from __future__ import annotations

import sutras  # noqa: F401 — register sutras

from engine.state import State, Term
from engine.dispatcher import apply_rule
from phonology.varna import parse_slp1_upadesha_sequence


def _dhatu_state(slp1: str) -> State:
    varnas = parse_slp1_upadesha_sequence(slp1)
    t = Term(
        kind="prakriti",
        varnas=varnas,
        tags={"prātipadika", "anga", "dhatu", "upadesha"},
        meta={"upadesha_slp1": slp1},
    )
    return State(terms=[t])


def test_bidir_irit_lopa_to_bid():
    s = _dhatu_state("Bidi~r")
    s = apply_rule("1.3.2", s)
    assert any("it_candidate_irit" in v.tags for t in s.terms for v in t.varnas)
    s = apply_rule("1.3.9", s)
    out = s.render()
    assert out == "Bid", f"expected Bid, got {out!r}"


def test_sup_su_tilde_strips_to_s():
    """Non-dhatu: anunāsika vowel fully elided (सुँ → स्)."""
    varnas = parse_slp1_upadesha_sequence("s~")
    t = Term(
        kind="pratyaya",
        varnas=varnas,
        tags={"upadesha", "sup"},
    )
    s = State(terms=[t])
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)
    assert s.render() == "s"
