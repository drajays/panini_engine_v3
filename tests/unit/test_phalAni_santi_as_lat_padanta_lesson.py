from __future__ import annotations


def test_phalAni_santi_flat_and_spine_order():
    from pipelines.phalAni_santi_as_lat_padanta_lesson import (
        derive_phalAni_santi_as_lat_padanta_lesson,
    )

    s = derive_phalAni_santi_as_lat_padanta_lesson()
    assert s.flat_slp1() == "phalAnisanti"
    assert [v.slp1 for v in s.terms[0].varnas] == ["p", "h", "a", "l", "A", "n", "i"]
    assert [v.slp1 for v in s.terms[1].varnas] == ["s", "a", "n", "t", "i"]

    ids = [
        e.get("sutra_id")
        for e in s.trace
        if e.get("sutra_id") not in ("__VERBAL_PADA_MERGE__",)
    ]
    assert ids.index("6.4.111") < ids.index("7.1.3")
    assert ids.index("7.1.3") < ids.index("1.1.58")
    assert ids.index("1.1.58") < ids.index("6.1.77")


def test_6_4_111_and_6_1_77_padanta_block():
    from pipelines.phalAni_santi_as_lat_padanta_lesson import (
        derive_phalAni_santi_as_lat_padanta_lesson,
    )

    s = derive_phalAni_santi_as_lat_padanta_lesson()
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.111"]
    assert s.paribhasha_gates.get("1_1_58_na_padAnta_etc") is True
    st677 = [e.get("status") for e in s.trace if e.get("sutra_id") == "6.1.77"]
    assert "APPLIED" not in st677
    assert "y" not in s.flat_slp1()


def test_6_1_77_would_fire_without_1_1_58_block():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    left = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("phalAni")),
        tags={"prātipadika"},
        meta={"upadesha_slp1": "phalAni"},
    )
    right = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("anti")),
        tags={"pratyaya", "tin_adesha_3_4_78"},
        meta={"upadesha_slp1": "anti"},
    )
    s = State(terms=[left, right], meta={}, trace=[])
    s = apply_rule("6.1.77", s)
    assert s.flat_slp1().startswith("phalAny")


def test_6_4_111_structural_on_as_before_jhi():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from core.canonical_pipelines import P00_tin_jhi_adesh_full

    as_d = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("as")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "as", "gana": 2},
    )
    s = State(terms=[as_d], meta={"lakara": "laT"}, trace=[])
    s = apply_rule("3.1.91", s)
    s = apply_rule("3.2.123", s)
    laT = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("la")),
        tags={"pratyaya", "lakAra_pratyaya_placeholder"},
        meta={"upadesha_slp1": "laT"},
    )
    s.terms.append(laT)
    s = P00_tin_jhi_adesh_full(s)
    s = apply_rule("1.2.4", s)
    s = apply_rule("6.4.111", s)
    assert [v.slp1 for v in s.terms[0].varnas] == ["s"]
    assert s.terms[0].meta.get("padadi_ac_lopa_para_nimitta") is True
