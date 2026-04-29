"""Narrow **6.4.16** (*ajjhanagamāṃ sani*) on *ci* + reduplication + *is*."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def test_6_4_16_lengthens_ci_and_strips_san_i() -> None:
    abhy = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ci"),
        tags={"dhatu", "anga", "abhyasa"},
        meta={"upadesha_slp1": "ci"},
    )
    main = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("ci"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "ci"},
    )
    san = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("is"),
        tags={"pratyaya", "sanadi", "ardhadhatuka"},
        meta={"upadesha_slp1": "is"},
    )
    s = State(terms=[abhy, main, san], meta={"6_4_16_sani_dirgha_arm": True}, trace=[])
    s = apply_rule("6.4.16", s)
    assert "".join(v.slp1 for v in s.terms[1].varnas) == "cI"
    assert "".join(v.slp1 for v in s.terms[2].varnas) == "s"
    assert (s.terms[2].meta.get("upadesha_slp1") or "").strip() == "s"
