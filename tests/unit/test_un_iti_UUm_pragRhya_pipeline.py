from __future__ import annotations


def test_u_ti_UUm_no_yan_or_eco_after_pragrahya():
    from pipelines.un_iti_UUm_pragRhya_demo import derive_U_ti_UUm_pragrahya
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

    s = derive_U_ti_UUm_pragrahya()
    assert "anunasika" in s.terms[0].varnas[0].tags
    assert s.terms[0].varnas[0].slp1 == "U"
    assert PRAGHYA_TERM_TAG in s.terms[0].tags
    assert s.flat_slp1() == "Uiti"


def test_u_ti_viti_when_no_pragrahya_iko_yan():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("u"),
        tags={"nipāta"},
        meta={},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={},
    )
    s = State(terms=[left, right], meta={"6_1_77_ik_yan_aci_general_arm": True}, trace=[])
    s = apply_rule("6.1.77", s)
    assert s.flat_slp1() == "viti"


def test_1_1_18_uum_skipped_without_anArSha():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from sutras.adhyaya_1.pada_1.sutra_1_1_18 import UUM_ADESA_ARM_META

    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("u"),
        tags={"nipāta"},
        meta={},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={},
    )
    s = State(terms=[left, right], meta={UUM_ADESA_ARM_META: True}, trace=[])
    s = apply_rule("1.1.18", s)
    assert s.terms[0].varnas[0].slp1 == "u"
