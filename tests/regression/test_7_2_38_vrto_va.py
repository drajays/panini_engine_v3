"""7.2.38 vṛto vā (Kāśikā): after vṛ (vṛñ, vṛṅ) and a ṝ-final dhātu the iṭ may be ī — varitā / varītā, taritā / tarītā; kariṣyati, hariṣyati (short ṛ) keep it short;
liṭ never lengthens (vavaritha); 7.2.39 bars the dīrgha in liṅ."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def forms(dhatu, lakara, pu=3, vac=1):
    return {b.surface_slp1 for b in explore(lambda: derive(dhatu, lakara, "kartari", pu, vac)) if "zz" not in b.surface_slp1}


@pytest.mark.parametrize("dhatu,short,long_", [("vfY", "varitA", "varItA"), ("vfN", "varitA", "varItA"), ("tF", "taritA", "tarItA"), ("jF", "jaritA", "jarItA")])
def test_iT_may_be_long(dhatu, short, long_):
    assert forms(dhatu, "luT") == {short, long_}


def test_sya_and_the_rest():
    assert forms("vfY", "lRT") == {"varizyati", "varIzyati"}
    assert forms("kf", "luT") == {"kartA"} and forms("kf", "lRT") == {"karizyati"}                  # short ṛ: not 'ṝkārānta'
    assert forms("hf", "lRT") == {"harizyati"}


def test_lit_is_not_lengthened_and_the_default_is_short():
    assert not any("I" in f for f in forms("tF", "liT"))                                                # tatAra …, no ī
    assert derive("vfY", "luT", "kartari", 3, 1).flat_slp1() == "varitA"                              # vibhāṣā: the default reading is the short iṭ


def test_7_2_39_and_7_2_40_bar_the_dirgha():
    """na liṅi (7.2.39): varisīṣṭa, not *varīsīṣṭa; sici ca parasmaipadeṣu (7.2.40): atāriṣṭām, avāriṣṭām — the iṭ of a parasmaipada sic stays short."""
    from engine.vikalpa import explore as _x

    def f(d, lakara, pu, vac, pada):
        return {b.surface_slp1 for b in _x(lambda: derive(d, lakara, "kartari", pu, vac, pada=pada)) if "zz" not in b.surface_slp1 and "Amm" not in b.surface_slp1}

    assert f("vfY", "AsIrliG", 3, 1, "atmane") == {"varizIzwa", "vfzIzwa"}      # no varIzIzwa; the iṭ-less vṛṣīṣṭa is 7.2.42
    assert f("tF", "luG", 3, 2, "parasmai") == {"atArizwAm"} and f("vfY", "luG", 3, 2, "parasmai") == {"avArizwAm"}
    assert f("tF", "luG", 3, 1, "atmane") == {"atarizwa", "atarIzwa", "atIrzwa"}                                 # ātmanepada: 7.2.38 is open again (7.2.42)


def test_7_2_42_and_7_2_43_make_the_iT_optional_in_atmanepada_ling_and_sic():
    """7.2.42 (vṛ, ṝ-final): vṛṣīṣṭa / variṣīṣṭa, avṛta / avariṣṭa / avarīṣṭa, āstīrṣṭa / āstariṣṭa / āstarīṣṭa;
    7.2.43 (short ṛ after a conjunct): smṛṣīṣṭa / smariṣīṣṭa, asmṛṣātām / asmariṣātām — smṛ is aniṭ by 7.2.10, the sūtra gives the iṭ back. kṛ (no conjunct) is untouched."""
    from engine.vikalpa import explore as _x

    def f(d, lakara, pu, vac, pada):
        return {b.surface_slp1 for b in _x(lambda: derive(d, lakara, "kartari", pu, vac, pada=pada))}

    assert f("vfY", "AsIrliG", 3, 1, "atmane") == {"varizIzwa", "vfzIzwa"}
    assert f("vfY", "luG", 3, 1, "atmane") == {"avfta", "avarizwa", "avarIzwa"}
    assert f("stF", "luG", 3, 1, "atmane") == {"astIrzwa", "astarizwa", "astarIzwa"}
    assert f("stF", "AsIrliG", 3, 1, "atmane") == {"stIrzIzwa", "starizIzwa"}
    assert f("smf", "AsIrliG", 3, 1, "atmane") == {"smfzIzwa", "smarizIzwa"}
    assert f("smf", "luG", 3, 2, "atmane") == {"asmfzAtAm", "asmarizAtAm"}
    assert f("kf", "AsIrliG", 3, 1, "atmane") == {"kfzIzwa"} and f("kf", "luG", 3, 1, "atmane") == {"akfta"}
    assert f("tF", "luG", 3, 2, "parasmai") == {"atArizwAm"}                                      # parasmaipada: neither sūtra
