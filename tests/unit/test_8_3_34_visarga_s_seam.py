"""8.3.34 visarjanīyasya saḥ across a pada seam (Kāśikā: vṛkṣaś chādayati, vṛkṣaṣ ṭīkate, vṛkṣas tarati); k/p stay for 8.3.37."""
import pytest
import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.pada_samhita import join_tripadi


@pytest.mark.parametrize("l,r,want", [("rAmas", "cinoti", "rAmaScinoti"), ("rAmas", "wIkate", "rAmazwIkate"), ("vfkzas", "tarati", "vfkzastarati"),
                                      ("vfkzas", "Cadayati", "vfkzaSCadayati"), ("rAmas", "TakArIyate", "rAmasTakArIyate")])
def test_8_3_34(l, r, want):
    assert want in {b.surface_slp1 for b in explore(lambda: join_tripadi(l, r))}


def test_ku_pu_not_8_3_34():
    assert {b.surface_slp1 for b in explore(lambda: join_tripadi("vfkzas", "karoti"))} == {"vfkzaHkaroti", "vfkzaZkaroti"}


def test_8_2_69_ahan_before_non_sup():
    assert "ahardadAti" in {b.surface_slp1 for b in explore(lambda: join_tripadi("ahan", "dadAti"))}
    assert {b.surface_slp1 for b in explore(lambda: join_tripadi("ahan", "karoti"))} == {"ahaHkaroti", "ahaZkaroti"}


def test_8_4_46_47_gemination_over_a_seam():
    got = {b.surface_slp1 for b in explore(lambda: join_tripadi("ahan", "dadAti", dvitva=True))}
    assert got == {"ahardadAti", "aharddadAti"}          # 8.4.46 aco rahābhyāṃ dve (r + d), once


def _s(l, r):
    return {b.surface_slp1 for b in explore(lambda: join_tripadi(l, r))}


def test_8_3_35_36_37():
    assert _s("vAsas", "kzOmam") == {"vAsaHkzOmam"}                         # 8.3.35 śarpare: ḥ stays
    assert _s("vfkzas", "SeTe") == {"vfkzaSSeTe", "vfkzaHSeTe"}             # 8.3.36 vā śari
    assert _s("vfkzas", "karoti") == {"vfkzaHkaroti", "vfkzaZkaroti"}       # 8.3.37 jihvāmūlīya
    assert _s("vfkzas", "Palati") == {"vfkzaHPalati", "vfkzaVPalati"}       # upadhmānīya


def test_3_4_109_jus_after_abhyasta():
    from pipelines.tinanta import derive
    for dh, want in (("02.0067", "ajAgaruH"), ("02.0068", "adaridruH")):
        s = derive(dh, "laG", "kartari", 3, 3)
        assert s.flat_slp1() == want and any(t["sutra_id"] == "3.4.109" and t["status"] == "APPLIED" for t in s.trace)
