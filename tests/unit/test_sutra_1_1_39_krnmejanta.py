from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _anga(s: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(s)),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": s},
    )


def _krt(s: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(s)),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": s},
    )


def test_1_1_39_m_anta_marks_avyaya() -> None:
    s0 = State(terms=[_anga("kAr"), _krt("am")])
    s1 = apply_rule("1.1.39", s0)
    assert "avyaya" in s1.terms[0].tags
    assert "avyaya" in s1.terms[1].tags


def test_1_1_39_ec_anta_marks_avyaya() -> None:
    s0 = State(terms=[_anga("vak"), _krt("se")])
    s1 = apply_rule("1.1.39", s0)
    assert "avyaya" in s1.terms[0].tags
    assert "avyaya" in s1.terms[1].tags

