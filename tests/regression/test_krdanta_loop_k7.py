"""K7 — the feminine of a kṛdanta: 4.1.6 ugitaś ca ṅīp after an ugit stem (Śatṛ: its ṛ), nuṃ before the nadī (7.1.81 Sap / Syan nityam,
7.1.80 vā after Sa, not after an abhyasta 7.1.78), 1.4.3 nadī on the ī, 6.1.68 su-lopa; and the ṭāp feminine of Śānac (4.1.4) reaching su-lopa."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

V = dict(kala="vartamAna", samAnADikaraRa="apraTamA")
CASES = [   # (dhātu id, vibhakti, vacana, form that must be one of the readings)
    ("01.0381", 1, 1, "paWantI"),      # पठन्ती (SK: pacantī)
    ("01.0381", 1, 2, "paWantyO"),
    ("01.0381", 2, 3, "paWantIH"),
    ("01.0381", 8, 1, "paWanti"),      # 7.3.107 hrasva
    ("01.0001", 1, 1, "BavantI"),
    ("04.0001", 1, 1, "divyantI"),     # Syan: nuṃ nitya
    ("06.0001", 1, 1, "tudantI"),      # Sa: 7.1.80 vā, both readings
    ("06.0001", 1, 1, "tudatI"),
    ("08.0010", 1, 1, "kurvatI"),      # u is not avarṇa: no nuṃ
    ("03.0001", 1, 1, "juhvatI"),      # 7.1.78 abhyasta: no nuṃ
    ("02.0001", 1, 1, "adatI"),        # Sap luk: the aṅga ad is not avarṇānta
    ("01.0002", 1, 1, "eDamAnA"),      # Śānac + ṭāp
]


@pytest.mark.parametrize("ref,vib,vac,want", CASES, ids=lambda c: None)
def test_feminine_participle(ref, vib, vac, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, vib, vac, "strīliṅga", **V))}
    assert want in got, sorted(got)


@pytest.mark.parametrize("ref,wrong", [("01.0381", "paWatI"), ("01.0001", "BavatI"), ("04.0001", "divyatI"), ("03.0001", "juhvantI")])
def test_no_nuM_wrongly(ref, wrong):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, "strīliṅga", **V))}
    assert wrong not in got, sorted(got)


@pytest.mark.parametrize("ref,vib,vac,want", [("01.0381", 1, 1, "paWitrI"), ("01.0381", 1, 2, "paWitryO"), ("01.0381", 8, 1, "paWitri"), ("01.1049", 1, 1, "netrI")])
def test_trc_feminine_4_1_5(ref, vib, vac, want):
    """4.1.5 ṛnnebhyo ṅīp: the tṛc stem ends in ṛ; the sup's aṅga is the ī, so 7.1.94 anaṅ stands aside (kartrī, not kartānī)."""
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, vib, vac, "strīliṅga", krt="Rvultfc"))}
    assert want in got and "paWitAnI" not in got, sorted(got)
