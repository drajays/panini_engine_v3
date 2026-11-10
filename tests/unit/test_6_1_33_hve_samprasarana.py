"""6.1.33 abhyastasya ca: ह्वे about to be doubled takes samprasāraṇa first (Kāśikā 6.1.33: "प्रागेव द्विर्वचनात् संप्रसारणं भवति। जुहाव"),
so 6.1.45 ātva finds no ec (paribhāṣā संप्रसारणं तदाश्रयं च कार्यं बलवत्, ORDER_BEFORE in engine/resolver.py)."""
from types import SimpleNamespace as NS

import sutras  # noqa: F401
from tools.autonomy_report import run_autonomously, start_state


def loop(ref, lak, pu, vc, pada=None):
    return run_autonomously(start_state(NS(kind="tinanta", args=(ref, lak, pu, vc), pada=pada)), "", ref, 250).surface


def recipe(upadesha, lak, pu, vc, pada=None):
    from pipelines.tinanta import derive
    return derive(upadesha, lak, "kartari", pu, vc, pada=pada).render()

HVE = "BvAdi_01_1163"


def test_loop_nal():
    assert loop(HVE, "liT", 3, 1, "parasmai") == "juhAva"
    assert loop(HVE, "liT", 1, 1, "parasmai") == "juhAva"


def test_loop_other_cells():
    assert loop(HVE, "liT", 3, 2, "parasmai") == "juhuvatuH"
    assert loop(HVE, "liT", 2, 1, "parasmai") == "juhaviTa"
    assert loop(HVE, "liT", 3, 1, "atmane") == "juhuve"


def test_recipe_derive_nal():
    assert recipe("hveY", "liT", 3, 1) == "juhAva"
    assert recipe("hveY", "liT", 3, 2) == "juhuvatuH"


def test_glai_still_atva():
    assert loop("BvAdi_01_1051", "liT", 3, 1, "parasmai") == "jaglO"
