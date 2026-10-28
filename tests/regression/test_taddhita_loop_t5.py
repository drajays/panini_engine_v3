"""T5 — 4.4: the ṭhak group (4.4.1 – 74): a sense (tena dīvyati …) opens a frame; ṭhak (4.4.1) attaches to the stems the opener admits, and the specials
(aṇ, ṭhañ, ṣṭhan, ṣṭhal, ṇya, ṭiṭhan, īkak …) take it over as apavādas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

VY, BH, SV = {"lex:vyaYjana"}, {"lex:Bakzya"}, {"lex:samavAya"}
CASES = [   # (stem, lexical tags, sense, extra vivakṣā, form that must be one of the readings)
    ("akza", None, "dIvyati", {}, "AkzikaH"),                           # 4.4.2 / 4.4.1
    ("aBrI", None, "Kanati", {}, "ABrikaH"),
    ("daDi", None, "tenasaMskfta", {}, "dADikaH"),                          # 4.4.3
    ("kulatTa", None, "tenasaMskfta", {}, "kOlatTaH"),                      # 4.4.4 aṇ
    ("uqupa", None, "tarati", {}, "OqupikaH"),                          # 4.4.5
    ("gopucCa", None, "tarati", {}, "gOpucCikaH"),                      # 4.4.6 ṭhañ
    ("nO", None, "tarati", {}, "nAvikaH"),                              # 4.4.7 ṣṭhan
    ("Gawa", None, "tarati", {}, "GawikaH"),                            # dvyac
    ("Akarza", None, "carati", {}, "AkarzikaH"),                        # 4.4.9 ṣṭhal
    ("parpa", None, "carati", {}, "parpikaH"),                          # 4.4.10
    ("SvagaRa", None, "carati", {}, "SvAgaRikaH"),                      # 4.4.11 ṭhañ
    ("SvagaRa", None, "carati", {}, "SvagaRikaH"),                      # ṣṭhan
    ("vetana", None, "jIvati", {}, "vEtanikaH"),                        # 4.4.12
    ("vasna", None, "jIvati", {}, "vasnikaH"),                          # 4.4.13
    ("AyuDa", None, "jIvati", {}, "AyuDIyaH"),                          # 4.4.14 cha
    ("AyuDa", None, "jIvati", {}, "AyuDikaH"),
    ("utsaNga", None, "harati", {}, "OtsaNgikaH"),                      # 4.4.15
    ("BastrA", None, "harati", {}, "BastrikaH"),                        # 4.4.16
    ("vivaDa", None, "harati", {}, "vivaDikaH"),                        # 4.4.17
    ("kuwilikA", None, "harati", {}, "kOwilikaH"),                      # 4.4.18
    ("akzadyUta", None, "tenanirvfta", {}, "AkzadyUtikaH"),                 # 4.4.19
    ("apamitya", None, "tenanirvfta", {}, "ApamityakaH"),                   # 4.4.21 kak
    ("yAcita", None, "tenanirvfta", {}, "yAcitakaH"),                       # kan
    ("cUrRa", None, "saMsfzwa", {}, "cUrRI"),                        # 4.4.23 ini
    ("mudga", None, "saMsfzwa", {}, "mOdgaH"),                          # 4.4.25
    ("daDi", VY, "upasikta", {}, "dADikaH"),                            # 4.4.26
    ("ojas", None, "vartate", {}, "OjasikaH"),                          # 4.4.27
    ("pratIpa", None, "vartate", {}, "prAtIpikaH"),                     # 4.4.28
    ("dviguRa", None, "prayacCati", {"arthaViSeSa": "garhya"}, "dvEguRikaH"),   # 4.4.30
    ("kusIda", None, "prayacCati", {"arthaViSeSa": "garhya"}, "kusIdikaH"),     # 4.4.31 ṣṭhan
    ("badara", None, "uYCati", {}, "bAdarikaH"),                        # 4.4.32
    ("samAja", None, "rakzati", {}, "sAmAjikaH"),                       # 4.4.33
    ("Sabda", None, "karoti", {}, "SAbdikaH"),                          # 4.4.34
    ("pakzin", None, "hanti", {}, "pAkzikaH"),                          # 4.4.35
    ("paripanTa", None, "tizWati", {}, "pAripanTikaH"),                 # 4.4.36
    ("daRqamATa", None, "DAvati", {}, "dARqamATikaH"),                  # 4.4.37
    ("Akranda", None, "DAvati", {}, "AkrandikaH"),                      # 4.4.38 ṭhañ ca
    ("pUrvapada", None, "gfhRAti", {}, "pOrvapadikaH"),                 # 4.4.39
    ("pratipaTa", None, "eti", {}, "pratipaTikaH"),                     # 4.4.42 ṭhan
    ("pratipaTa", None, "eti", {}, "prAtipaTikaH"),
    ("samAja", SV, "samavEti", {}, "sAmAjikaH"),                        # 4.4.43
    ("parizad", None, "samavEti", {}, "pArizadyaH"),                    # 4.4.44
    ("senA", None, "samavEti", {}, "sEnyaH"),                           # 4.4.45
    ("lalAwa", None, "paSyati", {"arthaViSeSa": "saMjYA"}, "lAlAwikaH"),     # 4.4.46
    ("SulkaSAlA", None, "Darmya", {}, "SOlkaSAlikaH"),                  # 4.4.47
    ("mahizI", None, "Darmya", {}, "mAhizaH"),                          # 4.4.48
    ("potf", None, "Darmya", {}, "pOtraH"),                             # 4.4.49 añ
    ("SulkaSAlA", None, "avakraya", {}, "SOlkaSAlikaH"),                # 4.4.50
    ("apUpa", None, "paRya", {}, "ApUpikaH"),                           # 4.4.51
    ("lavaRa", None, "paRya", {}, "lAvaRikaH"),                         # 4.4.52 ṭhañ
    ("mfdaNga", None, "Silpa", {}, "mArdaNgikaH"),                      # 4.4.55
    ("maqquka", None, "Silpa", {}, "mAqqukaH"),                         # 4.4.56
    ("asi", None, "praharaRa", {}, "AsikaH"),                           # 4.4.57
    ("paraSvaDa", None, "praharaRa", {}, "pAraSvaDikaH"),               # 4.4.58
    ("Sakti", None, "praharaRa", {}, "SAktIkaH"),                       # 4.4.59 īkak
    ("asti", None, "mati", {}, "AstikaH"),                              # 4.4.60
    ("nAsti", None, "mati", {}, "nAstikaH"),
    ("apUpa", None, "SIla", {}, "ApUpikaH"),                            # 4.4.61
    ("Catra", None, "SIla", {}, "CAtraH"),                              # 4.4.62 ṇa
    ("apUpa", BH, "hita", {}, "ApUpikaH"),                              # 4.4.65
    ("SrARA", None, "dIyate", {}, "SrARikaH"),                          # 4.4.67 ṭiṭhan
    ("Bakta", None, "dIyate", {}, "BAktaH"),                            # 4.4.68
    ("SulkaSAlA", None, "niyukta", {}, "SOlkaSAlikaH"),                 # 4.4.69
    ("devAgAra", None, "niyukta", {}, "devAgArikaH"),                   # 4.4.70 ṭhan
    ("prastAra", None, "vyavaharati", {}, "prAstArikaH"),               # 4.4.72
    ("nikawa", None, "vasati", {}, "nEkawikaH"),                        # 4.4.73
    ("AvasaTa", None, "vasati", {}, "AvasaTikaH"),                      # 4.4.74 ṣṭhal
]


@pytest.mark.parametrize("stem,og,sense,extra,want", CASES, ids=lambda c: None)
def test_sense(stem, og, sense, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "pulliṅga", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)


def test_no_frame_no_pratyaya():
    """The default ṭhak needs a sense frame that admits the stem (vartate: ojas, sahas … only), and aṇ has ended at 4.4.2 (prāg dīvyataḥ)."""
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("devadatta", 1, 1, "pulliṅga", taddhitArtha="vartate"))}
    assert all(s.startswith("devadatt") and s.endswith("aH") for s in got), sorted(got)      # no pratyaya (the extra readings are 8.4.46 doublings)
