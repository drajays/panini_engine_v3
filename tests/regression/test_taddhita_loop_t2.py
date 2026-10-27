"""T2 — the taddhita senses of 4.2: the sūtra that names a sense (tena raktam, nakṣatrayuktaḥ kālaḥ, tasya samūhaḥ …) takes aṇ or its apavāda; the
cāturarthika frame (4.2.67–70) and the śaiṣika frame (4.2.92) are opened by the vivakṣā and read by the specials after them. Kāśikā / Laghukaumudī."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

CASES = [   # (stem, lexical tags, sense, liṅga, form that must be one of the readings)
    ("kazAya", {"lex:rAga"}, "rakta", "pulliṅga", "kAzAyaH"),         # 4.2.1 aṇ
    ("lAkzA", {"lex:rAga"}, "rakta", "pulliṅga", "lAkzikaH"),         # 4.2.2 ṭhak (ṭh → ik 7.3.50)
    ("rohiRI", {"lex:nakzatra"}, "yukta", "pulliṅga", "rOhiRaH"),     # 4.2.3
    ("vasizWa", None, "dfzwa", "pulliṅga", "vAsizWaH"),               # 4.2.7
    ("kali", None, "dfzwa", "pulliṅga", "kAleyaH"),                   # 4.2.8 ḍhak
    ("vAmadeva", None, "dfzwa", "pulliṅga", "vAmadevyaH"),            # 4.2.9 ḍyat / ḍya (ṭi-lopa)
    ("vastra", None, "parivfta", "pulliṅga", "vAstraH"),              # 4.2.10
    ("pARqukambala", None, "parivfta", "pulliṅga", "pARqukambalI"),   # 4.2.11 ini
    ("dvEpa", None, "parivfta", "pulliṅga", "dvEpaH"),                # 4.2.12 añ
    ("SarAva", None, "udDfta", "pulliṅga", "SArAvaH"),                # 4.2.14
    ("indra", None, "devatA", "pulliṅga", "EndraH"),                  # 4.2.24
    ("soma", None, "devatA", "pulliṅga", "sOmyaH"),                   # 4.2.30 ṣyaṇ
    ("kAka", None, "samUha", "pulliṅga", "kAkaH"),                    # 4.2.37
    ("BikzA", None, "samUha", "pulliṅga", "BEkzaH"),                  # 4.2.38
    ("grAma", None, "samUha", "strīliṅga", "grAmatA"),                # 4.2.43 tal (talantaṃ strīliṅgam)
    ("naqa", None, "asti", "pulliṅga", "naqvalaH"),                   # 4.2.88 ḍvalac: the ṭi goes (6.4.143)
    ("SiKA", None, "asti", "pulliṅga", "SiKAvalaH"),                  # 4.2.89 valac
    ("vidiSA", None, "adUraBava", "pulliṅga", "vEdiSaH"),             # 4.2.70
    ("rAzwra", None, "Seza", "pulliṅga", "rAzwriyaH"),                # 4.2.93 gha beats vṛddhāc chaḥ
    ("avArapAra", None, "Seza", "pulliṅga", "avArapArIRaH"),          # 4.2.93 kha
    ("dakziRA", None, "Seza", "pulliṅga", "dAkziRAtyaH"),             # 4.2.98 tyak
    ("amA", None, "Seza", "pulliṅga", "amAtyaH"),                     # 4.2.104 tyap
    ("SAlA", None, "Seza", "pulliṅga", "SAlIyaH"),                    # 4.2.114 vṛddhāc chaḥ
    ("gaha", None, "Seza", "pulliṅga", "gahIyaH"),                    # 4.2.138
]


@pytest.mark.parametrize("stem,og,sense,linga,want", CASES, ids=lambda c: None)
def test_sense(stem, og, sense, linga, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, taddhitArtha=sense))}
    assert want in got, sorted(got)


def test_an_is_not_a_reading_where_its_apavada_stands():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("lAkzA", 1, 1, "pulliqga".replace("q", "ṅ"), origin_tags={"lex:rAga"}, taddhitArtha="rakta"))}
    assert "lAkzaH" not in got and "lAkzAH" not in got, sorted(got)
