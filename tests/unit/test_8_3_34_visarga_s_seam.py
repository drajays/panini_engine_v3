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
    assert {b.surface_slp1 for b in explore(lambda: join_tripadi("vfkzas", "karoti"))} == {"vfkzaHkaroti"}
