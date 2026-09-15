from __future__ import annotations


def test_yAyAvar_flat_and_spine_order():
    from pipelines.yAyAvar_yang_varac_purvavidhau_lesson import (
        derive_yAyAvar_yang_varac_purvavidhau_lesson,
    )

    s = derive_yAyAvar_yang_varac_purvavidhau_lesson()
    assert s.flat_slp1() == "yAyAvar"
    assert [v.slp1 for v in s.terms[0].varnas] == ["y", "A", "y", "A", "v", "a", "r"]

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id")]
    assert ids.index("6.4.48") < ids.index("1.1.57")
    assert ids.index("1.1.57") < ids.index("1.1.58")
    assert ids.index("1.1.58") < ids.index("6.4.64")
    assert ids.index("6.4.64") < ids.index("6.1.66")
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.1.66"]


def test_6_4_48_and_6_4_64_vareya_block():
    from pipelines.yAyAvar_yang_varac_purvavidhau_lesson import (
        derive_yAyAvar_yang_varac_purvavidhau_lesson,
    )
    from sutras.adhyaya_6.pada_4.sutra_6_4_48 import META_YA_G_A_LOPA

    s = derive_yAyAvar_yang_varac_purvavidhau_lesson()
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.48"]
    assert s.paribhasha_gates.get("1_1_58_na_padAnta_etc") is True
    st664 = [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.64"]
    assert "APPLIED" not in st664

    # Re-walk to stem just after 6.4.48 (before merge): meta on merged term in trace
    from pipelines.yAyAvar_yang_varac_purvavidhau_lesson import (
        _build_state,
        _merge_angas_with_yaG_a_before_varac,
    )
    from core.canonical_pipelines import (
        P00_bhuvadi_dhatu_it_anunasik_hal,
        P00_yang_adhikara_yaG_append_sanadi,
        P00_yang_dvitva_abhyasa_gate,
    )
    from engine import apply_rule

    s2 = _build_state()
    s2 = apply_rule("1.1.68", s2)
    s2 = P00_bhuvadi_dhatu_it_anunasik_hal(s2)
    s2 = P00_yang_adhikara_yaG_append_sanadi(s2)
    s2 = P00_yang_dvitva_abhyasa_gate(s2)
    s2.meta["varac_recipe"] = True
    s2 = apply_rule("3.2.176", s2)
    s2 = _merge_angas_with_yaG_a_before_varac(s2)
    s2 = apply_rule("6.4.48", s2)
    assert s2.terms[0].meta.get("6_4_48_a_lopa_done") is True
    assert s2.terms[0].meta.get(META_YA_G_A_LOPA) is True


def test_6_4_64_would_fire_without_1_1_58_block():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from sutras.adhyaya_6.pada_4.sutra_6_4_48 import META_YA_G_A_LOPA

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yA")),
        tags={"dhatu", "anga"},
        meta={
            "upadesha_slp1": "yA",
            "6_4_48_a_lopa_done": True,
            META_YA_G_A_LOPA: True,
        },
    )
    varac = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("varac")),
        tags={"pratyaya", "krt", "kngiti"},
        meta={"upadesha_slp1": "varac"},
    )
    s = State(terms=[stem, varac], meta={}, trace=[])
    s = apply_rule("1.1.57", s)
    s = apply_rule("6.4.64", s)
    assert [v.slp1 for v in s.terms[0].varnas] == ["y"]

    s2 = State(
        terms=[
            Term(
                kind="prakriti",
                varnas=list(parse_slp1_upadesha_sequence("yA")),
                tags={"dhatu", "anga"},
                meta={
                    "upadesha_slp1": "yA",
                    "6_4_48_a_lopa_done": True,
                    META_YA_G_A_LOPA: True,
                },
            ),
            varac,
        ],
        meta={},
        trace=[],
    )
    s2 = apply_rule("1.1.57", s2)
    s2 = apply_rule("1.1.58", s2)
    s2 = apply_rule("6.4.64", s2)
    assert [v.slp1 for v in s2.terms[0].varnas] == ["y", "A"]


def test_6_1_66_blocked_without_1_1_58_on_yAyAy_varac():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from sutras.adhyaya_6.pada_4.sutra_6_4_48 import META_YA_G_A_LOPA

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yAyAy")),
        tags={"dhatu", "anga"},
        meta={
            "upadesha_slp1": "yAyAy",
            "6_4_48_a_lopa_done": True,
            META_YA_G_A_LOPA: True,
        },
    )
    varac = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("varac")),
        tags={"krt", "pratyaya", "kngiti"},
        meta={"upadesha_slp1": "varac"},
    )
    s = State(terms=[stem, varac], meta={}, trace=[])
    s = apply_rule("1.1.57", s)
    s = apply_rule("6.1.66", s)
    assert [v.slp1 for v in s.terms[0].varnas][-1] == "y"

    s2 = State(terms=[stem, varac], meta={}, trace=[])
    s2 = apply_rule("1.1.57", s2)
    s2 = apply_rule("1.1.58", s2)
    s2 = apply_rule("6.1.66", s2)
    assert [v.slp1 for v in s2.terms[0].varnas] == ["y", "A", "y", "A"]


def test_6_4_48_structural_before_varac():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    stem = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("yAyAya")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "yAyAya"},
    )
    varac = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("varac")),
        tags={"krt", "pratyaya"},
        meta={"upadesha_slp1": "varac"},
    )
    s = State(terms=[stem, varac], meta={}, trace=[])
    s = apply_rule("6.4.48", s)
    assert [v.slp1 for v in s.terms[0].varnas] == ["y", "A", "y", "A", "y"]
