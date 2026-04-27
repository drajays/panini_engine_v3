from __future__ import annotations


def test_asme_indrAbfhaspatI_no_eco_78_after_she_pragrahya():
    from pipelines.asme_indrAbfhaspatI_pragRhya_demo import derive_asme_indrAbfhaspatI_pragrahya
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG

    s = derive_asme_indrAbfhaspatI_pragrahya()
    assert s.flat_slp1() == "asmeindrAbfhaspatI"
    assert [v.slp1 for v in s.terms[0].varnas][-1] == "e"
    assert PRAGHYA_TERM_TAG in s.terms[0].tags


def test_tve_iti_no_eco_78_after_she_pragrahya():
    from pipelines.asme_indrAbfhaspatI_pragRhya_demo import derive_tve_iti_pragrahya

    s = derive_tve_iti_pragrahya()
    assert s.flat_slp1() == "tveiti"


def test_me_iti_no_eco_78_after_she_pragrahya():
    from pipelines.asme_indrAbfhaspatI_pragRhya_demo import derive_me_iti_pragrahya

    s = derive_me_iti_pragrahya()
    assert s.flat_slp1() == "meiti"


def test_1_1_11_she_arm_tags_only_e_final_anga():
    import sutras  # noqa: F401
    from engine import apply_rule
    from engine.state import State, Term
    from phonology import mk
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG, SHE_PRAGHYA_TAG_ARM_META

    a = Term(
        kind="prakriti",
        varnas=[mk("a"), mk("s"), mk("m"), mk("e")],
        tags={"anga", "prātipadika"},
        meta={},
    )
    noise = Term(
        kind="prakriti",
        varnas=[mk("g"), mk("a"), mk("c"), mk("a"), mk("t"), mk("i")],
        tags={"anga", "prātipadika"},
        meta={},
    )
    s = State(terms=[a, noise], meta={SHE_PRAGHYA_TAG_ARM_META: True}, samjna_registry={})
    s = apply_rule("1.1.11", s)
    assert PRAGHYA_TERM_TAG in s.terms[0].tags
    assert PRAGHYA_TERM_TAG not in s.terms[1].tags
