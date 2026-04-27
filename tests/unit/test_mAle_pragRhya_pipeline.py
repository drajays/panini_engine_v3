from __future__ import annotations


def test_mAle_iti_no_eco_ayavAyAva_across_pragrahya():
    from pipelines.mAle_iti_pragRhya_demo import derive_mAle_iti_pragrahya

    s = derive_mAle_iti_pragrahya()
    assert s.flat_slp1() == "mAleiti"
    assert [v.slp1 for v in s.terms[0].varnas] == ["m", "A", "l", "e"]
    assert s.samjna_registry.get("6.1.125_prakRti_aci") == 1


def test_mAle_iti_eco_78_would_apply_without_pragrahya_tag():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mAle"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "mAlA"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    s = apply_rule("6.1.78", s)
    assert s.flat_slp1() == "mAlayiti"
