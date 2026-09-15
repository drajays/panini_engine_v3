from __future__ import annotations


def test_agaty_flat_and_spine_order():
    from pipelines.agaty_gam_lyap_acah_lesson import derive_agaty_gam_lyap_acah_lesson

    s = derive_agaty_gam_lyap_acah_lesson()
    assert s.flat_slp1() == "Agaty"

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id") not in ("__MERGE__", "__MERGE_PREP__")]
    assert ids.index("3.4.21") < ids.index("7.1.37")
    assert ids.index("7.1.37") < ids.index("6.4.38")
    assert ids.index("6.4.38") < ids.index("1.3.9")
    assert ids.index("1.3.9") < ids.index("6.1.71")
    assert ids.index("6.1.71") < ids.index("1.1.57")


def test_6_4_38_m_lopa_then_tuk_despite_1_1_57():
    from pipelines.agaty_gam_lyap_acah_lesson import derive_agaty_gam_lyap_acah_lesson

    s = derive_agaty_gam_lyap_acah_lesson()
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.38"]
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.1.71"]
    assert s.paribhasha_gates.get("1.1.57_aca_parasmin_purvavidhau") is True
    assert "t" in s.flat_slp1()


def test_6_4_38_structural_m_lopa_on_lyap():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence
    from phonology import mk

    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("lyap")),
        tags={"pratyaya", "krt"},
        meta={"upadesha_slp1": "lyap"},
    )
    for i, v in enumerate(pr.varnas):
        if v.slp1 == "l":
            pr.varnas.insert(i + 1, mk("m"))
            break
    s = State(terms=[pr], meta={}, trace=[])
    s = apply_rule("6.4.38", s)
    pr = s.terms[0]
    assert [v.slp1 for v in pr.varnas] == ["l", "y", "a", "p"]
    assert pr.meta.get("6_4_38_m_lopa_done") is True
    assert pr.meta.get("hal_lupta_not_ac_sthanivat") is True
