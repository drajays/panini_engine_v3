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
