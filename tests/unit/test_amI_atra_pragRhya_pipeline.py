from __future__ import annotations


def test_amI_atra_no_iko_yan_across_pragrahya():
    from pipelines.amI_atra_pragRhya_demo import derive_amI_atra_pragrahya

    s = derive_amI_atra_pragrahya()
    assert s.flat_slp1() == "amIatra"
    assert s.terms[0].varnas[-1].slp1 == "I"
    assert s.samjna_registry.get("6.1.125_prakRti_aci") == 1


def test_amI_atra_iko_77_applies_without_pragrahya_tag():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("amI"),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": "adas"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("atra"),
        tags={"nipāta"},
        meta={},
    )
    s = State(terms=[left, right], meta={"6_1_77_ik_yan_aci_general_arm": True}, trace=[])
    s = apply_rule("6.1.77", s)
    assert s.flat_slp1() == "amyatra"
