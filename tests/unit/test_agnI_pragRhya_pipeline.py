from __future__ import annotations


def test_agnI_iti_no_dIrgha_across_pragrahya():
    from pipelines.agnI_iti_pragRhya_demo import derive_agnI_iti_pragrahya

    s = derive_agnI_iti_pragrahya()
    assert s.flat_slp1() == "agnIiti"
    assert s.samjna_registry.get("6.1.125_prakRti_aci") == 1


def test_vAyU_iti_no_iko_yan_across_pragrahya():
    from pipelines.agnI_iti_pragRhya_demo import derive_vAyU_iti_no_yan

    s = derive_vAyU_iti_no_yan()
    assert s.flat_slp1() == "vAyUiti"
    assert s.terms[0].varnas[-1].slp1 == "U"


def test_vAyu_dual_surface_vAyU_after_pUrvasavarNa():
    import sutras  # noqa: F401
    from pipelines.subanta import build_initial_state, run_subanta_pipeline

    s = build_initial_state("vAyu", 1, 2, "pulliṅga")
    s = run_subanta_pipeline(s)
    assert s.flat_slp1() == "vAyU"


def test_agni_dual_anga_tagged_pragrahya_after_pUrvasavarNa():
    """**6.1.102** then **1.1.11** tags ``pragrahya`` on the *aṅga* before *pada* merge."""
    import sutras  # noqa: F401
    from engine import apply_rule
    from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG
    from pipelines.subanta import (
        PADA_MERGE_STEP,
        SUBANTA_RULE_IDS_POST_4_1_2,
        _pada_merge,
        build_initial_state,
        run_subanta_preflight_through_1_4_7,
    )

    s = build_initial_state("agni", 1, 2, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    for sid in SUBANTA_RULE_IDS_POST_4_1_2:
        if sid == PADA_MERGE_STEP:
            break
        s = apply_rule(sid, s)
        if sid == "1.1.11" and s.flat_slp1().startswith("agnI"):
            anga = next(t for t in s.terms if "anga" in t.tags)
            assert PRAGHYA_TERM_TAG in anga.tags
            return
    raise AssertionError("expected 1.1.11 after 6.1.102 with agnI surface")
