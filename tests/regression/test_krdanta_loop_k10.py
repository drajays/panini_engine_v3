"""K10 — upapada kṛts beyond aṇ: 3.2.16 caraṭ, 3.2.17 bhikṣā-senā-ādāya, 3.2.20 kṛñ ṭa, 3.2.38 khac, 3.2.78 ṇini, 3.2.83 khaś / ṇini, 3.2.85 yaj ṇini,
3.2.94 / 3.2.96 kvanip (Kāśikā and Laghukaumudī udāharaṇas); the apavādas take the site from aṇ (3.2.1) and from niṣṭhā (3.2.102)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta

BH = dict(kala="BUta", artha="kartf")
CASES = [   # (dhātu, upapada, linga, vivakṣā, form that must be one of the readings)
    ("cara~", ("kuru", "aDikaraRa"), "pulliṅga", {}, "kurucaraH"),         # कुरुचरः
    ("cara~", ("kuru", "aDikaraRa"), "strīliṅga", {}, "kurucarI"),         # कुरुचरी (4.1.15: ṭit)
    ("cara~", ("BikzA", "karman"), "pulliṅga", {}, "BikzAcaraH"),          # 3.2.17
    ("cara~", ("senA", "karman"), "pulliṅga", {}, "senAcaraH"),
    ("qukfY", ("yaSas", "karman"), "pulliṅga", dict(hetutAcCIlyAnulomya="hetu"), "yaSaskaraH"),      # 3.2.20 (not aṇ: yaśaskāra)
    ("qukfY", ("SrAdDa", "karman"), "pulliṅga", dict(hetutAcCIlyAnulomya="tAcCIlya"), "SrAdDakaraH"),
    ("vada~", ("priya", "karman"), "pulliṅga", {}, "priyamvadaH"),         # 3.2.38 khac + mum
    ("vada~", ("vaSa", "karman"), "pulliṅga", {}, "vaSamvadaH"),
    ("Buja~", ("uzRa", "karman"), "pulliṅga", dict(tAcCIlya="tAcCIlya"), "uzRaBojI"),             # 3.2.78
    ("mana~", ("paRqita", "karman"), "pulliṅga", dict(AtmamAna="AtmamAna"), "paRqitamAnI"),       # 3.2.83 ṇini
    ("mana~", ("paRqita", "karman"), "pulliṅga", dict(AtmamAna="AtmamAna"), "paRqitammanyaH"),    # 3.2.83 khaś (Syan, mum)
    ("yaja~", ("agniztoma", "karaRa"), "pulliṅga", BH, "agnizwomayAjI"),                           # 3.2.85
    ("dfSi~r", ("pAra", "karman"), "pulliṅga", BH, "pAradfSvA"),                                    # 3.2.94
    ("yuDa~", ("saha", "karman"), "pulliṅga", BH, "sahayuDvA"),                                     # 3.2.96
    ("dfSi~r", ("pAra", "karman"), "pulliṅga", BH, "pAradfStavAn"),                                 # niṣṭhā stays beside the special kṛt
]


@pytest.mark.parametrize("ref,up,linga,kw,want", CASES, ids=lambda c: None)
def test_upapada_krdanta(ref, up, linga, kw, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, 1, 1, linga, upapada=up, **kw))}
    assert want in got, sorted(got)


def test_apavada_takes_the_site_from_an():
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta("qukfY", 1, 1, "pulliṅga", upapada=("yaSas", "karman"), hetutAcCIlyAnulomya="hetu"))}
    assert "yaSaskAraH" not in got, sorted(got)
