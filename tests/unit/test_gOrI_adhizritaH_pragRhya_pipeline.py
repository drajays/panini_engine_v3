from __future__ import annotations


def test_gOrI_aDiSritaH_no_yan_across_pragrahya():
    from pipelines.gOrI_adhizritaH_pragRhya_demo import derive_gOrI_aDiSritaH_pragrahya
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

    s = derive_gOrI_aDiSritaH_pragrahya()
    assert s.flat_slp1() == "gOrIaDiSritaH"
    assert PRAGHYA_TERM_TAG in s.terms[0].tags
    assert s.terms[0].varnas[-1].slp1 == "I"


def test_mAmakI_iti_no_yan():
    from pipelines.gOrI_adhizritaH_pragRhya_demo import derive_mAmakI_iti_pragrahya

    s = derive_mAmakI_iti_pragrahya()
    assert s.flat_slp1() == "mAmakIiti"


def test_tanU_iti_no_yan():
    from pipelines.gOrI_adhizritaH_pragRhya_demo import derive_tanU_iti_pragrahya

    s = derive_tanU_iti_pragrahya()
    assert s.flat_slp1() == "tanUiti"


def test_gOrI_aDiSritaH_yan_without_saptamyartha_pragrahya_tag():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("gOrI"),
        tags={"anga", "prātipadika"},
        meta={},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("aDiSritaH"),
        tags={"anga", "prātipadika"},
        meta={},
    )
    s = State(terms=[left, right], meta={"6_1_77_ik_yan_aci_general_arm": True}, trace=[])
    s = apply_rule("6.1.77", s)
    assert s.flat_slp1() == "gOryaDiSritaH"


def test_1_1_19_arm_tags_I_U_only():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG, PRAGHYA_VOWEL_SLP1
    from sutras.adhyaya_1.pada_1.sutra_1_1_19 import SAPTAMYARTHA_PRAGHYA_TAG_ARM_META

    g = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("gOrI"),
        tags={"prātipadika", "anga"},
        meta={},
    )
    noise = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("rAma"),
        tags={"prātipadika", "anga"},
        meta={},
    )
    s = State(
        terms=[g, noise],
        meta={SAPTAMYARTHA_PRAGHYA_TAG_ARM_META: True},
        samjna_registry={"pragrahya": PRAGHYA_VOWEL_SLP1},
    )
    s = apply_rule("1.1.19", s)
    assert PRAGHYA_TERM_TAG in s.terms[0].tags
    assert PRAGHYA_TERM_TAG not in s.terms[1].tags
