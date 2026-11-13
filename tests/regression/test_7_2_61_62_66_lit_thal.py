"""liṭ thal and the nityānit roots: 7.2.61 (ac-final) and 7.2.62 (a-vat) give the iṭ-less reading beside 7.2.63's niyama reading (Kāśikā 7.2.63: 'pūrvayor yogayor vikalpaḥ');
7.2.66 keeps the iṭ for ad, ṛ, vyay; 2.4.40 is optional (ghasl or ad: jaghāsa / āda)."""
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.tinanta import derive


def forms(d, pu=2, vac=1, lakara="liT"):
    return {b.surface_slp1 for b in explore(lambda: derive(d, lakara, "kartari", pu, vac))}


def test_ac_final_nityanit_thal_has_both_readings():
    assert forms("yA") == {"yayATa", "yayiTa"} and {f for f in forms("hu") if not any(x in f for x in ("AYca", "AmAs", "AmbaB"))} == {"juhoTa", "juhaviTa"}    # + the ām readings of 3.1.39 (juhavāñcakartha) and forms("ciY") == {"ciceTa", "cicayiTa"}


def test_a_vat_nityanit_thal_has_both_readings():
    assert {"papakTa", "peciTa"} <= forms("qupaca~z") and forms("yaja~") == {"iyazWa", "iyajiTa"}


def test_other_cells_and_ri_roots_are_untouched():
    assert forms("yA", 3, 1) == {"yayO"} and forms("kfY") == {"cakarTa"}


def test_7_2_66_ad_ri_vyay_keep_the_it_and_2_4_40_is_optional():
    assert forms("ada~") == {"AdiTa", "jaGasiTa"} and forms("ada~", 1, 1) == {"Ada", "jaGAsa"} and forms("ada~", 3, 2) == {"AdatuH", "jakzatuH"}
    assert forms("f") == {"AriTa"} and forms("vyaya~") == {"vavyayiTa"}
