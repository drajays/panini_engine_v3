"""
Gold prakriyā — *jayati* step 1: *ji* + **1.1.60** / **1.3.1** / **1.3.2**–**1.3.9** / **1.3.10**.
"""
from __future__ import annotations

import json
from pathlib import Path

import sutras  # noqa: F401

from sutras.adhyaya_1.pada_1.lopa_samjna_1_1_60 import LOPA_REGISTER_VALUE, LOPA_SAMJNA_KEY

from tools.tinanta_jayati_gold import (
    JAYATI_DHATU_ROW_ID,
    STEP_1_RULE_IDS,
    STEP_2_RULE_IDS,
    STEP_3_IT_RULE_IDS,
    STEP_4_POST_77_RULE_IDS,
    STEP_5_RULE_IDS,
    STEP_6_IT_RULE_IDS,
    STEP_7_RULE_IDS,
    STEP_8_RULE_IDS,
    STEP_9_TRIPADI_AUDIT_RULE_IDS,
    build_ji_dhatu_state,
    run_jayati_gold_step1,
    run_jayati_gold_step2,
    run_jayati_gold_step3,
    run_jayati_gold_step4,
    run_jayati_gold_step5,
    run_jayati_gold_step6,
    run_jayati_gold_step7,
    run_jayati_gold_step8,
    run_jayati_gold_step9,
    run_jayati_gold_through_step,
    term_has_any_it_marker,
)

from sutras.adhyaya_1.pada_4.dvi_eka_1_4_22 import DVI_EKA_NIMITTA_KEY
from sutras.adhyaya_1.pada_4.tin_tripartite_1_4_101 import TIN_101_TAG_TRIPARTITE_A
from sutras.adhyaya_1.pada_4.tin_vacana_1_4_102 import TIN_102_TAG_EKA
from sutras.adhyaya_3.pada_1.vikarana_sap_3_1_68 import SAP_INSERT_TAG
from engine import apply_rule
from sutras.adhyaya_3.pada_4.sutra_3_4_113 import SARVADHATUKA_113

_GOLD = Path(__file__).resolve().parents[2] / "data" / "reference" / "tinanta_gold" / "jayati_prakriya.json"


def test_gold_sarani_md_beside_json() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    name = spec.get("gold_sarani")
    assert name == "jayati_gold_sarani.md"
    path = _GOLD.parent / name
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert "जयति" in text
    assert "3.1.91" in text or "३.१.९१" in text


def test_step1_keeps_ji_surface() -> None:
    s = run_jayati_gold_step1()
    assert s.flat_slp1() == "ji"
    assert len(s.terms) == 1
    assert "dhatu" in s.terms[0].tags
    assert not term_has_any_it_marker(s.terms[0])


def test_step1_dhatu_samjna_and_lopa_register() -> None:
    s = run_jayati_gold_step1()
    assert s.samjna_registry.get("1.3.1_bhuvadi_dhatu") is True
    assert s.samjna_registry.get(LOPA_SAMJNA_KEY) == LOPA_REGISTER_VALUE


def test_step1_trace_includes_core_sutras() -> None:
    from engine.trace import TRACE_STATUSES_FIRED

    s = run_jayati_gold_step1()
    ids = [e.get("sutra_id") for e in s.trace if e.get("status") in TRACE_STATUSES_FIRED]
    assert "1.1.60" in ids
    assert "1.3.1" in ids
    assert "1.3.10" in ids


def test_step1_1_3_9_vacuous_when_dhatu_has_no_it() -> None:
    """
    *ji* has no *it* letter (after 1.3.1–1.3.8): **1.3.9** is still a checked
    *vidhi* (Issue 7 — *APPLIED_VACUOUS*, not *COND-FALSE*).
    """
    s = run_jayati_gold_step1()
    e19 = [e for e in s.trace if e.get("sutra_id") == "1.3.9"][-1]
    assert e19.get("status") == "APPLIED_VACUOUS"
    assert e19.get("lopa_count") == 0
    assert e19.get("form_before") == e19.get("form_after") == "ji"
    assert e19.get("skip_reason") is None


def test_build_from_dhatupatha_row_meta() -> None:
    s = build_ji_dhatu_state()
    assert s.terms[0].meta.get("dhatupatha_id") == JAYATI_DHATU_ROW_ID
    assert s.terms[0].meta.get("upadesha_slp1") == "ji"
    assert s.terms[0].meta.get("karmakatva") == "akarmaka"


def test_json_step1_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][0]["rule_ids"])
    assert got == STEP_1_RULE_IDS


def test_json_step2_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][1]["rule_ids"])
    assert got == STEP_2_RULE_IDS


def test_step2_checkpoint_ji_plus_laT() -> None:
    s = run_jayati_gold_step2()
    assert len(s.terms) == 2
    assert s.terms[0].meta.get("upadesha_slp1") == "ji"
    assert s.terms[1].meta.get("upadesha_slp1") == "laT"
    assert "laT" in s.flat_slp1()
    assert "ji" in s.flat_slp1() or s.flat_slp1().startswith("j")


def test_step2_vivaksha_meta_and_gates() -> None:
    s = run_jayati_gold_step2()
    v = s.meta.get("gold_jayati_vivaksha")
    assert v is not None
    assert v.get("prayoga") == "kartari"
    assert s.paribhasha_gates.get("prayoga_3_4_69_licenses_kartari") is True


def test_step2_adhikara_stack_keeps_lat_scope() -> None:
    s = run_jayati_gold_step2()
    ids = [e.get("id") for e in s.adhikara_stack]
    assert "3.2.123" in ids


def test_through_step2_equals_step2() -> None:
    assert run_jayati_gold_through_step(2).flat_slp1() == run_jayati_gold_step2().flat_slp1()


def test_json_step3_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][2]["rule_ids"])
    assert got == STEP_3_IT_RULE_IDS


def test_step3_checkpoint_jil_and_laT_meta() -> None:
    s = run_jayati_gold_step3()
    assert s.flat_slp1() == "jil"
    assert len(s.terms) == 2
    assert s.terms[1].meta.get("upadesha_slp1") == "laT"
    assert [v.slp1 for v in s.terms[1].varnas] == ["l"]
    assert s.terms[1].meta.get("gold_lat_post_it_lac") is True
    assert "upadesha" in s.terms[1].tags


def test_step3_halantyam_registry_for_laT() -> None:
    s = run_jayati_gold_step3()
    assert ("it_halantyam", 1) in s.samjna_registry


def test_step3_no_it_markers_remain() -> None:
    s = run_jayati_gold_step3()
    for t in s.terms:
        assert not term_has_any_it_marker(t)


def test_through_step3_equals_step3() -> None:
    assert run_jayati_gold_through_step(3).flat_slp1() == run_jayati_gold_step3().flat_slp1()


def test_json_step4_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][3]["rule_ids_after_lat"])
    assert got == STEP_4_POST_77_RULE_IDS


def test_step4_checkpoint_ji_tip() -> None:
    s = run_jayati_gold_step4()
    assert len(s.terms) == 2
    assert s.terms[0].meta.get("upadesha_slp1") == "ji"
    assert s.terms[1].meta.get("upadesha_slp1") == "tip"
    assert "tip" in s.flat_slp1()
    assert "parasmaipada" in s.terms[1].tags
    assert TIN_101_TAG_TRIPARTITE_A in s.terms[1].tags
    assert TIN_102_TAG_EKA in s.terms[1].tags
    assert s.terms[0].meta.get(DVI_EKA_NIMITTA_KEY) == "eka"


def test_step4_adhikara_3_4_77_on_stack() -> None:
    s = run_jayati_gold_step4()
    assert any(e.get("id") == "3.4.77" for e in s.adhikara_stack)


def test_through_step4_equals_step4() -> None:
    assert run_jayati_gold_through_step(4).flat_slp1() == run_jayati_gold_step4().flat_slp1()


def test_json_step5_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][4]["rule_ids"])
    assert got == STEP_5_RULE_IDS


def test_step5_checkpoint_ji_Sap_tip() -> None:
    s = run_jayati_gold_step5()
    assert len(s.terms) == 3
    assert [t.meta.get("upadesha_slp1") for t in s.terms] == ["ji", "Sap", "tip"]
    assert s.flat_slp1() == "jiSaptip"
    assert "upadesha" in s.terms[1].tags
    assert "vikarana" in s.terms[1].tags
    assert SAP_INSERT_TAG in s.terms[1].tags
    assert SARVADHATUKA_113 in s.terms[2].tags
    assert any(e.get("id") == "3.1.91" for e in s.adhikara_stack)


def test_through_step5_equals_step5() -> None:
    assert run_jayati_gold_through_step(5).flat_slp1() == run_jayati_gold_step5().flat_slp1()


def test_json_step6_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][5]["rule_ids"])
    assert got == STEP_6_IT_RULE_IDS


def test_step6_checkpoint_jiati_after_it_lopa() -> None:
    s = run_jayati_gold_step6()
    assert s.flat_slp1() == "jiati"
    assert [t.meta.get("upadesha_slp1") for t in s.terms] == ["ji", "Sap", "tip"]
    assert ["".join(v.slp1 for v in t.varnas) for t in s.terms] == ["ji", "a", "ti"]
    for t in s.terms:
        assert not term_has_any_it_marker(t)


def test_step6_samjna_1_3_3_and_1_3_8_no_flat_change_lopa_at_1_3_9() -> None:
    """
    *Halantyam* (1.3.3) and *laśakavataddhite* (1.3.8) are *saṃjñā* (no *flat* change);
    *lopa* of ``S`` and both ``p`` is **1.3.9** only (Issue 2).
    """
    s = run_jayati_gold_step5()
    assert s.flat_slp1() == "jiSaptip"
    for sid in STEP_6_IT_RULE_IDS:
        fb = s.flat_slp1()
        s = apply_rule(sid, s)
        fa = s.flat_slp1()
        if sid == "1.3.3":
            assert fb == fa == "jiSaptip", (sid, fb, fa)
        if sid == "1.3.8":
            assert fb == fa == "jiSaptip", (sid, fb, fa)
        if sid == "1.3.9":
            assert fb == "jiSaptip" and fa == "jiati", (fb, fa)
    assert s.flat_slp1() == "jiati"


def test_through_step6_equals_step6() -> None:
    assert run_jayati_gold_through_step(6).flat_slp1() == run_jayati_gold_step6().flat_slp1()


def test_json_step7_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][6]["rule_ids"])
    assert got == STEP_7_RULE_IDS


def test_step7_checkpoint_jeati_guna() -> None:
    s = run_jayati_gold_step7()
    assert s.flat_slp1() == "jeati"
    assert ["".join(v.slp1 for v in t.varnas) for t in s.terms] == ["je", "a", "ti"]
    assert "anga" in s.terms[0].tags
    assert s.terms[0].meta.get("anga_guna_7_3_84") is True
    assert s.samjna_registry.get(("1.4.13_anga", 0)) == frozenset({"active"})
    assert any(e.get("id") == "6.4.1" for e in s.adhikara_stack)


def test_through_step7_equals_step7() -> None:
    assert run_jayati_gold_through_step(7).flat_slp1() == run_jayati_gold_step7().flat_slp1()


def test_json_step8_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][7]["rule_ids"])
    assert got == STEP_8_RULE_IDS


def test_step8_checkpoint_jayati() -> None:
    s = run_jayati_gold_step8()
    assert s.flat_slp1() == "jayati"
    assert ["".join(v.slp1 for v in t.varnas) for t in s.terms] == ["jay", "a", "ti"]
    assert s.terms[0].meta.get("eco_ayavayava_done") is True
    last3 = [e for e in s.trace if e.get("sutra_id") in ("6.1.72", "6.1.77", "6.1.78")]
    st = {e.get("sutra_id"): e.get("status") for e in last3 if e.get("sutra_id")}
    assert st.get("6.1.72") == "AUDIT"
    assert st.get("6.1.77") == "SKIPPED"
    assert st.get("6.1.78") == "APPLIED"


def test_through_step8_equals_step8() -> None:
    assert run_jayati_gold_through_step(8).flat_slp1() == run_jayati_gold_step8().flat_slp1()


def test_json_step9_rule_ids_match_module() -> None:
    spec = json.loads(_GOLD.read_text(encoding="utf-8"))
    got = tuple(spec["steps"][8]["rule_ids"])
    assert got == STEP_9_TRIPADI_AUDIT_RULE_IDS


def test_step9_tripadi_audit_jayati_unchanged() -> None:
    s = run_jayati_gold_step9()
    assert s.flat_slp1() == "jayati"
    assert s.tripadi_zone is True
    assert any(e.get("id") == "8.1.16" for e in s.adhikara_stack)
    assert any(e.get("id") == "8.2.1" for e in s.adhikara_stack)
    assert s.meta.get("gold_jayati_step9_tripadi_audit", {}).get("tripadi_8_2_1") is True
    last83 = [e for e in s.trace if e.get("sutra_id") in ("8.1.16", "8.2.1", "8.2.66")]
    st = {e.get("sutra_id"): e.get("status") for e in last83 if e.get("sutra_id")}
    assert st.get("8.1.16") == "AUDIT"
    assert st.get("8.2.1") == "AUDIT"
    assert st.get("8.2.66") == "SKIPPED"


def test_through_step9_equals_step9() -> None:
    assert run_jayati_gold_through_step(9).flat_slp1() == run_jayati_gold_step9().flat_slp1()
