"""Cluster C (exercise audit): 6.1.59 am vā, 6.4.62 ciṇvadiṭ, 1.2.2 vij iṭ ṅidvat, iṭ-initial kit liṭ of vye / hve (6.4.148 needs bha)."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive
from tools.autonomy_report import run_autonomously, start_state


def _forms(*a, **k):
    return {b.surface_slp1 for b in explore(lambda: derive(*a, **k))}


def _trace_status(branches, sid):
    return {t.get("status") for b in branches for t in b.state.trace if t.get("sutra_id") == sid}


def _loop(ref, lak, pu, vc, pada=None):
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface


def test_6_1_59_am_vibhasha_kraSTA():
    assert {"krazwA", "karzwA"} <= _forms("06.0006", "luT", "kartari", 3, 1)        # kf\za~^ is anudātta, ṛ-upadha, tAs is jhal-initial and not kit
    assert {"sprazwAsi", "sparzwAsi"} <= _forms("06.0158", "luT", "kartari", 2, 1)


def test_6_4_62_cinvadit_karmani_lrt():
    assert {"BAvizyate", "Bavizyate"} <= _forms("01.0001", "lRT", "karmani", 3, 1)
    assert "pArizyate" in _forms("03.0005", "lRT", "karmani", 3, 1)                # ajanta aṅga: ciṇvat vṛddhi + iṭ, then 1.1.51 rapara


def test_6_4_62_not_in_kartari():
    assert _forms("01.0001", "lRT", "kartari", 3, 1) == {"Bavizyati"}


def test_1_2_2_vij_it_is_ngidvat_by_the_sutra():
    branches = list(explore(lambda: derive("07.0023", "liT", "kartari", 2, 1)))
    assert {b.surface_slp1 for b in branches} == {"vivijiTa"}
    assert "APPLIED" in _trace_status(branches, "1.2.2")                           # 7.2.35 no longer does 1.2.2's work for it


def test_kit_lit_of_vye_hve_keeps_the_y_and_v():
    VYE, HVE = "BvAdi_01_1162", "BvAdi_01_1163"
    assert _loop(VYE, "liT", 1, 2, "parasmai") == "vivyiva"                        # 6.4.148 is bhasya: the aṅga of a tiṅ is not bha
    assert _loop(VYE, "liT", 1, 3, "parasmai") == "vivyima"
    assert _loop(VYE, "liT", 3, 3, "atmane") == "vivyire"
    assert _loop(HVE, "liT", 1, 2, "parasmai") == "juhuviva"


# --- padas lexicon stems: viśva + rāj / viśva + vah + ṇvi keep their parts apart on the tape ---
def _cell(stem, vib, vac, linga="pulliṅga"):
    from pipelines.subanta import derive
    return {b.surface_slp1.replace("SS", "S").replace("qq", "q") for b in explore(lambda: derive(stem, vib, vac, linga=linga))}


def test_6_3_128_viSva_rAj_lengthens_only_before_the_rAw():
    assert {"viSvArAq", "viSvArAw"} <= _cell("viSvarAj", 1, 1)           # DB: viśvarāḍ / viśvarāṭ (6.3.128 before 8.2.36)
    assert "viSvArAqByAm" in _cell("viSvarAj", 3, 2)
    assert _cell("viSvarAj", 1, 2) == {"viSvarAjO"} and _cell("viSvarAj", 1, 3) == {"viSvarAjaH"}     # Kāśikā: viśvarājau, viśvarājaḥ


def test_6_4_132_6_1_89_viSvavAh():
    assert "viSvOhaH" in _cell("viSvavAh", 2, 3) and "viSvOhA" in _cell("viSvavAh", 3, 1)       # DB: viśvauhaḥ, viśvauhā
    assert "viSvavAqByAm" in _cell("viSvavAh", 3, 2)                                                # not bha before a consonant sup


# --- 6.1.32 hvaH samprasAraRam (ṇau ca sanścaṅoḥ): hve before a ṇic that a san / caṅ follows — hand-built tapes, like the Kāśikā's ---
def _hve_tape(after):
    from engine.state import State, Term
    from phonology import mk

    def t(slp1, up, *tags, kind="pratyaya", mula=False):
        vs = [mk(c) for c in slp1]
        if mula:
            vs[-1].tags.add("mula_dhatu_v")
        return Term(kind=kind, varnas=vs, tags=set(tags), meta={"upadesha_slp1": up})
    return State(terms=[t("hve", "hveY", "dhatu", "anga", kind="prakriti", mula=True), t("i", "Ric", "pratyaya"), t("a", after, "pratyaya")])


def test_6_1_32_hve_before_Nic_then_san_or_caN():
    from engine import apply_rule
    for after in ("san", "caN"):
        s = apply_rule("6.1.32", _hve_tape(after))
        assert s.terms[0].meta.get("samprasarana_done")                      # 1.1.45 will turn its v into u (juhāvayiṣati, ajūhavat)
    s = apply_rule("6.1.32", _hve_tape("ap"))                                 # no san / caṅ after the ṇic: nothing
    assert not s.terms[0].meta.get("samprasarana_done")


# --- añc stems [upasarga][ac] (6.4.24 at kvin, 6.4.138/139, 6.3.93/94/138, 7.1.70, 8.2.62) ---
def test_anc_stems_weak_and_strong():
    assert "prAcaH" in _cell("prAYc", 2, 3) and "prAYcaH" in _cell("prAYc", 1, 3) and "prAN" in _cell("prAYc", 1, 1)
    assert "udIcaH" in _cell("udaYc", 2, 3) and "udaYcaH" in _cell("udaYc", 1, 3) and "udagByAm" in _cell("udaYc", 3, 2)   # 6.4.139
    assert "pratIcaH" in _cell("pratyaYc", 2, 3) and "pratyaYcaH" in _cell("pratyaYc", 1, 3)                              # 6.3.138
    assert "samIcaH" in _cell("samyaYc", 2, 3) and "samyaYcaH" in _cell("samyaYc", 1, 3)                                  # 6.3.93
    assert "tiryaN" in _cell("tiryaYc", 1, 1) and "tiraScaH" in _cell("tiryaYc", 2, 3) and "tiryagBiH" in _cell("tiryaYc", 3, 3)   # 6.3.94
    assert "udakzu" in _cell("udaYc", 7, 3) and "gIrzu" in _cell("gIr", 7, 3, "strīliṅga")                                  # su is not yaci: no bha
