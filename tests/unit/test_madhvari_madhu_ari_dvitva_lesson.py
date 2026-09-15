from __future__ import annotations

from sutras.adhyaya_6.pada_1.sutra_6_1_77 import IKO_YANACI_ADESHA_TAG


def test_maddhvari_flat_and_spine_order():
    from pipelines.madhvari_madhu_ari_dvitva_lesson import (
        derive_madhvari_madhu_ari_dvitva_lesson,
    )

    s = derive_madhvari_madhu_ari_dvitva_lesson()
    assert s.flat_slp1() == "maddhvari"

    ids = [e.get("sutra_id") for e in s.trace if e.get("status") == "APPLIED"]
    assert ids.index("6.1.77") < ids.index("1.1.58")
    assert ids.index("1.1.58") < ids.index("8.4.47")


def test_yan_only_madhvari_without_dvitva():
    from pipelines.madhvari_madhu_ari_dvitva_lesson import (
        derive_madhvari_madhu_ari_yan_only_lesson,
    )

    s = derive_madhvari_madhu_ari_yan_only_lesson()
    assert s.flat_slp1() == "madhvari"
    assert "APPLIED" not in [
        e.get("status") for e in s.trace if e.get("sutra_id") == "8.4.47"
    ]


def test_6_1_77_tags_yan_adesha_and_8_4_47_doubles_d_not_v():
    from pipelines.madhvari_madhu_ari_dvitva_lesson import (
        derive_madhvari_madhu_ari_dvitva_lesson,
    )

    s = derive_madhvari_madhu_ari_dvitva_lesson()
    madhu = s.terms[0]
    assert madhu.meta.get("para_nimitta_yan_adesha") is True
    assert IKO_YANACI_ADESHA_TAG in madhu.varnas[-1].tags
    assert [v.slp1 for v in madhu.varnas] == ["m", "a", "d", "d", "h", "v"]
    assert s.paribhasha_gates.get("1_1_58_na_padAnta_etc") is True
    assert "APPLIED" in [e.get("status") for e in s.trace if e.get("sutra_id") == "8.4.47"]


def test_8_4_47_skips_gemination_of_yan_adesha_varna():
    import sutras  # noqa: F401

    from engine import apply_rule
    from engine.state import State, Term
    from phonology.varna import parse_slp1_upadesha_sequence

    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("mavari")),
        tags=set(),
        meta={},
    )
    v = t.varnas[2]
    v.tags.add(IKO_YANACI_ADESHA_TAG)
    s = State(terms=[t], meta={}, trace=[])
    s.tripadi_zone = True
    s = apply_rule("8.2.108", s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.4.47", s)
    assert [x.slp1 for x in s.terms[0].varnas].count("v") == 1
