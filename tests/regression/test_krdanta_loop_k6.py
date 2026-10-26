"""K6 — the present participle: śatṛ / śānac stand in laṭ's place (3.2.124, vartamāne + apraTamāsamānādhikaraṇe) and the loop does the rest — śap and
the other vikaraṇas before a śit kṛt (3.1.68 ff.), nuṃ (7.1.70), muk (7.2.82). Forms are Kāśikā udāharaṇas (pacantaṃ caitraṃ paśya, pacamānam)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

V = dict(kala="vartamAna", samAnADikaraRa="apraTamA")
CASES = [   # (dhātu id, vibhakti, vacana, liṅga, form that must be one of the readings)
    ("01.0381", 2, 1, "pulliṅga", "paWantam"),      # पठन्तम्
    ("01.0381", 1, 1, "pulliṅga", "paWan"),
    ("01.0381", 3, 1, "pulliṅga", "paWatA"),
    ("01.0381", 1, 1, "napuṃsaka", "paWat"),
    ("01.0001", 2, 1, "pulliṅga", "Bavantam"),      # भवन्तम् (śap, guṇa, ay-av)
    ("08.0010", 2, 1, "pulliṅga", "kurvantam"),     # 3.1.79 u before a śit kṛt
    ("05.0001", 2, 1, "pulliṅga", "sunvantam"),     # 3.1.73 śnu
    ("06.0001", 2, 1, "pulliṅga", "tudantam"),      # 3.1.77 śa
    ("09.0001", 2, 1, "pulliṅga", "krIRantam"),     # 3.1.81 śnā
    ("04.0001", 2, 1, "pulliṅga", "divyantam"),     # 3.1.69 śyan
    ("01.0002", 2, 1, "pulliṅga", "eDamAnam"),      # ātmanepada: śānac, 7.2.82 muk
    ("06.0001", 2, 1, "pulliṅga", "tudamAnam"),     # ubhayapadī: the other reading
    ("08.0010", 2, 1, "pulliṅga", "kurvARam"),      # śānac after u: no muk, ṇatva
]


@pytest.mark.parametrize("ref,vib,vac,linga,want", CASES, ids=lambda c: None)
def test_present_participle(ref, vib, vac, linga, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, vib, vac, linga, **V))}
    assert want in got, sorted(got)


@pytest.mark.xfail(reason="strī-pratyaya ṅīp for an ugit kṛt (4.1.6) is a gate-only stub; paWantI not derived", strict=True)
def test_feminine_not_yet():
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta("01.0381", 1, 1, "strīliṅga", **V))}
    assert "paWantI" in got, sorted(got)
