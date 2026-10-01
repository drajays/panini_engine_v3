from __future__ import annotations


def test_agaty_flat_and_spine_order():
    from pipelines.agaty_gam_lyap_acah_lesson import derive_agaty_gam_lyap_acah_lesson

    s = derive_agaty_gam_lyap_acah_lesson()
    assert s.flat_slp1() == "Agatya"
    assert s.flat_dev() == "आगत्य"

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id") not in ("__MERGE__", "__MERGE_PREP__")]
    after_lyap = ids[ids.index("7.1.37"):]
    assert ids.index("3.4.21") < ids.index("7.1.37")
    assert after_lyap.index("6.4.38") < after_lyap.index("1.3.9")
    assert after_lyap.index("1.3.9") < after_lyap.index("6.1.71")
    assert after_lyap.index("6.1.71") < after_lyap.index("1.1.57")


def test_tape_starts_from_upadesha_gamx():
    from pipelines.agaty_gam_lyap_acah_lesson import derive_agaty_gam_lyap_acah_lesson

    s = derive_agaty_gam_lyap_acah_lesson()
    first = next(e for e in s.trace if e.get("form_before"))
    assert first["form_before"].startswith("Agamx")


def test_6_4_38_m_lopa_then_tuk_despite_1_1_57():
    from pipelines.agaty_gam_lyap_acah_lesson import derive_agaty_gam_lyap_acah_lesson

    s = derive_agaty_gam_lyap_acah_lesson()
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.38"]
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.1.71"]
    assert s.paribhasha_gates.get("1.1.57_aca_parasmin_purvavidhau") is True
    assert "t" in s.flat_slp1()


def test_6_4_38_drops_dhatu_final_m_not_a_lyap_varna():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    dh = Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence("gam")),
              tags={"dhatu", "anga"}, meta={"upadesha_slp1": "gamx~", "udatta_dhatu": False})
    pr = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("lyap")),
              tags={"pratyaya", "krt"}, meta={"upadesha_slp1": "lyap"})
    s = apply_rule("6.4.38", State(terms=[dh, pr], meta={}, trace=[]))
    assert [v.slp1 for v in s.terms[0].varnas] == ["g", "a"]
    assert [v.slp1 for v in s.terms[1].varnas] == ["l", "y", "a", "p"]
    assert s.terms[0].meta.get("hal_lupta_not_ac_sthanivat") is True


def test_6_4_38_not_for_udatta_upadesha_dhatu():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    dh = Term(kind="prakriti", varnas=list(parse_slp1_upadesha_sequence("kram")),
              tags={"dhatu", "anga"}, meta={"upadesha_slp1": "kramu~", "udatta_dhatu": True})
    pr = Term(kind="pratyaya", varnas=list(parse_slp1_upadesha_sequence("lyap")),
              tags={"pratyaya", "krt"}, meta={"upadesha_slp1": "lyap"})
    s = apply_rule("6.4.38", State(terms=[dh, pr], meta={}, trace=[]))
    assert [v.slp1 for v in s.terms[0].varnas] == ["k", "r", "a", "m"]
