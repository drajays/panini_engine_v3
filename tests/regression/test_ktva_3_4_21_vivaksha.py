"""3.4.21 समानकर्तृकयोः पूर्वकाले attaches ktvā only when both meanings are intended (Kāśikā 3.4.21).

भुक्त्वा व्रजति — earlier action, same agent: ktvā. Pratyudāharaṇa: भुक्तवति ब्राह्मणे व्रजति देवदत्तः (two agents);
व्रजति च जल्पति च (not earlier) — no ktvā.
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.tape_init.krdanta import PURVAKALA_SAMANAKARTRKA, build_krdanta_state
from pipelines.krdanta import build_dhatu_state


def _Buj(**vivaksha):
    return build_dhatu_state("ruDAdi_07_0017", **vivaksha)      # भुजँ पालनाभ्यवहारयोः


def test_udaharana_attaches_the_upadesha_ktva():
    s = apply_rule("3.4.21", _Buj(**PURVAKALA_SAMANAKARTRKA))
    pr = s.terms[-1]
    assert pr.kind == "pratyaya" and {"krt", "upadesha"} <= pr.tags
    assert pr.meta["upadesha_slp1"] == "ktvA"
    assert "".join(v.slp1 for v in pr.varnas) == "ktvA"


@pytest.mark.parametrize("vivaksha", [
    {"kala": "pUrvakAla"},                          # भुक्तवति ब्राह्मणे व्रजति देवदत्तः
    {"samAnakartfka": "samAnakartfka"},             # व्रजति च जल्पति च
    {},
])
def test_pratyudaharana_attach_nothing(vivaksha):
    assert not SUTRA_REGISTRY["3.4.21"].cond(_Buj(**vivaksha))


def test_attached_once():
    s = apply_rule("3.4.21", _Buj(**PURVAKALA_SAMANAKARTRKA))
    assert not SUTRA_REGISTRY["3.4.21"].cond(s)


def test_lyap_spines_start_from_3_4_21_once():
    """ashtadhyayi.com prakriyā under 1.1.56: प्र + पठ् + क्त्वा → ल्यप् → प्रपठ्य; Kāśikā 7.1.37: प्रकृत्य."""
    from pipelines.prakftya_lyap_split_prakriyas import derive_prakftya_lyap_split_prakriyas_P017
    from pipelines.sthanivat_anal_ashrita_lesson import derive_pra_paW_lyap_avyaya

    for derive, form in ((derive_pra_paW_lyap_avyaya, "prapaWya"), (derive_prakftya_lyap_split_prakriyas_P017, "prakftya")):
        s = derive()
        assert s.flat_slp1() == form
        assert [e.get("sutra_id") for e in s.trace if isinstance(e, dict)].count("3.4.21") == 1


def test_cond_reads_no_recipe_flag():
    s = build_krdanta_state(_Buj().terms)
    s.meta["ktvA_recipe"] = True
    assert not SUTRA_REGISTRY["3.4.21"].cond(s)
