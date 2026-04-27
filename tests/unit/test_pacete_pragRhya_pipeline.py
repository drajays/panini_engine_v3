from __future__ import annotations


def test_pacete_iti_no_eco_ayavAyAva_across_pragrahya():
    from pipelines.pacete_iti_pragRhya_demo import derive_pacete_iti_pragrahya

    s = derive_pacete_iti_pragrahya()
    assert s.flat_slp1() == "paceteiti"
    assert [v.slp1 for v in s.terms[0].varnas] == ["p", "a", "c", "e", "t", "e"]
    assert s.samjna_registry.get("6.1.125_prakRti_aci") == 1


def test_pacete_iti_eco_78_applies_without_pragrahya_tag():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("pacete"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "qupac~z"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    s = apply_rule("6.1.78", s)
    # Final *aṅga* vowel is the last *e* of *…te*; *e*+*i* → *a*+*y*+*i* (6.1.78).
    assert s.flat_slp1() == "pacetayiti"
