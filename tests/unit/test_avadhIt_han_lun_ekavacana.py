from __future__ import annotations

def test_avadhIt_flat_and_spine_order():
    from pipelines.avadhIt_han_lun_ekavacana_lesson import (
        derive_avadhIt_han_lun_ekavacana_lesson,
    )

    s = derive_avadhIt_han_lun_ekavacana_lesson()
    assert s.flat_slp1() == "avadhIt"

    ids = [e.get("sutra_id") for e in s.trace if e.get("sutra_id") not in ("__MERGE__",)]
    assert ids.index("2.4.43") < ids.index("6.4.71")
    assert ids.index("6.4.71") < ids.index("3.4.78")
    assert ids.index("7.2.35") < ids.index("6.4.48")
    assert ids.index("6.4.48") < ids.index("1.1.57")
    assert ids.index("1.1.57") < ids.index("7.2.7")
    assert ids.index("3.4.100") < ids.index("7.3.96")
    assert ids.index("8.2.28") < ids.index("6.1.101")


def test_vadh_a_lopa_blocks_anga_vrddhi():
    from pipelines.avadhIt_han_lun_ekavacana_lesson import (
        derive_avadhIt_han_lun_ekavacana_lesson,
    )

    s = derive_avadhIt_han_lun_ekavacana_lesson()
    assert s.paribhasha_gates.get("1.1.57_aca_parasmin_purvavidhau") is True
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "6.4.48"]
    flat = s.flat_slp1()
    assert "vadh" in flat

    st7 = [e.get("status") for e in s.trace if e.get("sutra_id") == "7.2.7"]
    assert "APPLIED" not in st7


def test_6_4_48_structural_on_vadh_before_ardhadhatuka():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    dhatu = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("vadha"),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "vadha"},
    )
    sic = Term(
        kind="pratyaya",
        varnas=parse_slp1_upadesha_sequence("sic"),
        tags={"pratyaya", "ardhadhatuka"},
        meta={"upadesha_slp1": "sic"},
    )
    s = State(terms=[dhatu, sic], meta={}, trace=[])
    s = apply_rule("6.4.48", s)
    assert "".join(v.slp1 for v in s.terms[0].varnas) == "vadh"
    assert s.terms[0].meta.get("6_4_48_a_lopa_done") is True
