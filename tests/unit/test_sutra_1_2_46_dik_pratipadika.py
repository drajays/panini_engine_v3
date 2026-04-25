from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology    import mk


def test_1_2_46_records_samjna_on_merged_dik_samasa():
    merged = Term(
        kind="prakriti",
        varnas=[mk("u")],
        tags={"prātipadika", "anga", "diksamasa", "bahuvrihi"},
        meta={"upadesha_slp1": "uttarapUrvA"},
    )
    s0 = State(terms=[merged])
    s1 = apply_rule("1.2.46", s0)
    assert s1.samjna_registry.get("1.2.46_dik_pratipadika") is True
    assert len(s1.terms) == 1
    assert {"diksamasa", "bahuvrihi", "prātipadika"}.issubset(s1.terms[0].tags)
