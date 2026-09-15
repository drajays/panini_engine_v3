from __future__ import annotations


def test_kaNDUti_flat_and_spine_order():
    from pipelines.kaNDUti_ktic_vareya_yalopa_lesson import (
        derive_kaNDUti_ktic_vareya_yalopa_lesson,
    )

    s = derive_kaNDUti_ktic_vareya_yalopa_lesson()
    assert s.flat_slp1() == "kaNDUti"
    assert [v.slp1 for v in s.terms[0].varnas] == ["k", "a", "N", "D", "U", "t", "i"]

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id")]
    assert ids.index("3.3.174") < ids.index("6.4.48")
    assert ids.index("6.4.48") < ids.index("1.1.57")
    assert ids.index("1.1.57") < ids.index("1.1.58")
    assert ids.index("1.1.58") < ids.index("6.1.66")


def test_6_4_48_and_6_1_66_vareya_yalopa():
    from pipelines.kaNDUti_ktic_vareya_yalopa_lesson import (
        derive_kaNDUti_ktic_vareya_yalopa_lesson,
    )
    from sutras.adhyaya_6.pada_4.sutra_6_4_48 import META_KTIC_A_LOPA

    s = derive_kaNDUti_ktic_vareya_yalopa_lesson()
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.48"]
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.1.66"]
    assert s.paribhasha_gates.get("1_1_58_na_padAnta_etc") is True

    from pipelines.kaNDUti_ktic_vareya_yalopa_lesson import _build_state
    from core.canonical_pipelines import P06a_pratyaya_adhikara_3_1_1_to_3
    from engine import apply_rule

    s2 = _build_state()
    s2 = apply_rule("3.1.91", s2)
    s2 = P06a_pratyaya_adhikara_3_1_1_to_3(s2)
    s2.meta["ktic_3_3_174_recipe"] = True
    s2 = apply_rule("3.3.174", s2)
    s2 = apply_rule("6.4.48", s2)
    assert s2.terms[0].meta.get("6_4_48_a_lopa_done") is True
    assert s2.terms[0].meta.get(META_KTIC_A_LOPA) is True


def test_6_1_66_blocked_without_1_1_58_after_6_4_48():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from sutras.adhyaya_6.pada_4.sutra_6_4_48 import META_KTIC_A_LOPA

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kaNDUy")),
        tags={"dhatu", "anga"},
        meta={
            "upadesha_slp1": "kaNDUy",
            "6_4_48_a_lopa_done": True,
            META_KTIC_A_LOPA: True,
        },
    )
    krt = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ktic")),
        tags={"krt", "pratyaya", "kngiti"},
        meta={"upadesha_slp1": "ktic"},
    )
    s = State(terms=[stem, krt], meta={}, trace=[])
    s = apply_rule("1.1.57", s)
    s = apply_rule("6.1.66", s)
    assert [v.slp1 for v in s.terms[0].varnas][-1] == "y"

    s2 = State(terms=[stem, krt], meta={}, trace=[])
    s2 = apply_rule("1.1.57", s2)
    s2 = apply_rule("1.1.58", s2)
    s2 = apply_rule("6.1.66", s2)
    assert [v.slp1 for v in s2.terms[0].varnas] == ["k", "a", "N", "D", "U"]


def test_6_1_66_yalopa_before_t_after_it_lopa():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kaNDUy")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "kaNDUy", "6_4_48_a_lopa_done": True},
    )
    ti = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("ti")),
        tags={"krt", "pratyaya", "kngiti"},
        meta={"upadesha_slp1": "ti"},
    )
    s = State(terms=[stem, ti], meta={}, trace=[])
    s.paribhasha_gates["1_1_58_na_padAnta_etc"] = True
    s = apply_rule("6.1.66", s)
    assert [v.slp1 for v in s.terms[0].varnas] == ["k", "a", "N", "D", "U"]
