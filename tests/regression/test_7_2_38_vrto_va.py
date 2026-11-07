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
