"""3.4.92 आडुत्तमस्य पिच्च (Kāśikā: "स च उत्तमपुरुषः पिद् भवति"): the Aṭ-ed loṭ uttama is pit, so 1.2.4 does not make it ṅidvat and
7.3.84 guṇa applies to bibhI + Ani. 6.4.82 (aci yaṇ) and 7.3.84 are a real vipratiṣedha (para = 7.3.84): the Aṭ is the first part of the
pratyaya (1.1.46), so the guṇa's nimitta is not bahiraṅga to the yaṇ's."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


def loop(ref, lak, pu, vc, pada=None):
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface


def recipe(upadesha, lak, pu, vc, pada=None):
    from pipelines.tinanta import derive
    return derive(upadesha, lak, "kartari", pu, vc, pada=pada).render()

BHI = "JuhotyAdi_03_0002"


def test_loop_uttama_loT():
    assert loop(BHI, "loT", 1, 1) == "biBayAni"
    assert loop(BHI, "loT", 1, 2) == "biBayAva"
    assert loop(BHI, "loT", 1, 3) == "biBayAma"


def test_ngit_forms_unchanged():
    assert loop(BHI, "loT", 3, 2) == "biBItAm"
    assert loop(BHI, "loT", 3, 3) == "biByatu"


def test_recipe_derive():
    assert recipe("YiBI", "loT", 1, 1) == "biBayAni"
