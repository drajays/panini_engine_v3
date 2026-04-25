"""
Step 1 bootstrap: 1.4.45 adhikaraṇa → 2.3.36 saptamī → 4.1.2 sup (ङि / Ni).

This test uses the **opt-in** meta flag on 2.3.36 so existing recipes that
explicitly provide vibhakti/vacana remain unchanged.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_4.sutra_1_4_45 import META_LOCUS_INDICES, SAMJNA_KEY
from sutras.adhyaya_2.pada_3.sutra_2_3_36 import META_AUTO_SET_VIBHAKTI_VACANA


def test_adhikarana_sets_vibhakti_vacana_then_4_1_2_attaches_ngi():
    shala = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("SAlA"),
        tags={"anga"},
        meta={"upadesha_slp1": "SAlA"},
    )
    s = State(terms=[shala])

    # Step 0.1
    s = apply_rule("1.2.45", s)
    assert "prātipadika" in s.terms[0].tags

    # Step 1.1 (caller provides locus analysis)
    s = apply_rule("1.4.23", s)
    s.meta[META_LOCUS_INDICES] = (0,)
    s = apply_rule("1.4.45", s)
    assert isinstance(s.samjna_registry.get(SAMJNA_KEY), frozenset)

    # Step 1.2 (opt-in: derive vibhakti-vacana)
    s.meta[META_AUTO_SET_VIBHAKTI_VACANA] = True
    s = apply_rule("2.3.36", s)
    assert s.meta.get("vibhakti_vacana") == "7-1"

    # Step 1.3–1.4 (sup attachment from prātipadika)
    s = apply_rule("4.1.1", s)
    s = apply_rule("4.1.2", s)
    assert any("sup" in t.tags for t in s.terms)
    sup = [t for t in s.terms if "sup" in t.tags][0]
    assert sup.meta.get("upadesha_slp1") == "Ni"

