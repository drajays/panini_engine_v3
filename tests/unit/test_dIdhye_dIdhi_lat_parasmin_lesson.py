from __future__ import annotations


def test_dIdhye_flat_and_spine_order():
    from pipelines.dIdhye_dIdhi_lat_parasmin_lesson import (
        derive_dIdhye_dIdhi_lat_parasmin_lesson,
    )

    s = derive_dIdhye_dIdhi_lat_parasmin_lesson()
    assert s.flat_slp1() == "dIdhye"

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id") not in ("__MERGE__",)]
    assert ids.index("3.2.123") < ids.index("3.4.78")
    assert ids.index("3.1.68") < ids.index("2.4.72")
    assert ids.index("2.4.72") < ids.index("3.4.79")
    assert ids.index("3.4.79") < ids.index("1.1.57")
    assert ids.index("1.1.57") < ids.index("7.4.53")
    assert ids.index("7.4.53") < ids.index("6.1.77")


def test_7_4_53_blocked_after_sva_nimitta_e():
    from pipelines.dIdhye_dIdhi_lat_parasmin_lesson import (
        derive_dIdhye_dIdhi_lat_parasmin_lesson,
    )

    s = derive_dIdhye_dIdhi_lat_parasmin_lesson()
    assert s.paribhasha_gates.get("1.1.57_aca_parasmin_purvavidhau") is True
    st753 = [e.get("status") for e in s.trace if e.get("sutra_id") == "7.4.53"]
    assert "APPLIED" not in st753
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "3.4.79"]
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.1.77"]


def test_7_4_53_would_fire_on_ii_before_i_not_e():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    dh = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("dIdhI")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "dIdhI"},
    )
    tin = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("i")),
        tags={"pratyaya", "tin_adesha_3_4_78"},
        meta={"upadesha_slp1": "i"},
    )
    s = State(terms=[dh, tin], meta={}, trace=[])
    s = apply_rule("7.4.53", s)
    assert [v.slp1 for v in s.terms[0].varnas] == ["d", "I", "d", "h"]
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "7.4.53"]
