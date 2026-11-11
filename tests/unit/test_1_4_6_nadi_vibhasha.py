"""1.4.4–1.4.6 + 7.3.117 (Kāśikā): the iyaṅuvaṅsthāna yU stems and the hrasva strī i/u stems take nadī optionally before ṅit sups.
Every reading is checked as a set (the geminated variants explore() also shows are the 8.4.46 branch, not asserted here)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.subanta import derive


def readings(stem, vib, vac):
    return {b.surface_slp1 for b in explore(lambda: derive(stem, vib, vac, linga="strīliṅga"))}


CASES = [
    # (stem, vibhakti, vacana, forms that must be present, forms that must be absent)
    ("mati", 4, 1, {"mataye", "matyE"}, set()),               # 1.4.6: kṛtyai, kṛtaye
    ("mati", 5, 1, {"mateH", "matyAH"}, set()),
    ("mati", 7, 1, {"matO", "matyAm"}, set()),                # 7.3.117
    ("Denu", 4, 1, {"Denave", "DenvE"}, set()),
    ("Denu", 7, 1, {"DenO", "DenvAm"}, set()),
    ("SrI", 1, 1, {"SrIH"}, {"SrI"}),                          # the ī of a kvip dhātu is no ṅī: su stays (hē śrīḥ)
    ("SrI", 4, 1, {"Sriye", "SriyE"}, {"SryE"}),               # 1.4.4/1.4.6: śriyai, śriye
    ("SrI", 5, 1, {"SriyaH", "SriyAH"}, {"SryAH"}),
    ("SrI", 6, 3, {"SriyAm", "SrIRAm"}, set()),                # 1.4.5 vā āmi
    ("SrI", 7, 1, {"Sriyi", "SriyAm"}, {"Sri"}),               # 6.4.148 needs ī, not the i of ṅi
    ("devI", 4, 1, {"devyE"}, {"devaye"}),                     # a long nadī: no vibhāṣā
    ("nadI", 6, 3, {"nadInAm"}, set()),
]


@pytest.mark.parametrize("stem,vib,vac,yes,no", CASES)
def test_nadi_vibhasha(stem, vib, vac, yes, no):
    got = readings(stem, vib, vac)
    assert yes <= got, (stem, vib, vac, sorted(got))
    assert not (no & got), (stem, vib, vac, sorted(got))
