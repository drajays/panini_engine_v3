"""T14b — 5.3.61 – 119 (the svārthika pratyayas): rūpap / kalpap / deśya / deśīya / jātīyar (5.3.66 – 69), the ka adhikāra 5.3.70 – 95 (senses ajñāta, kutsita,
anukampā, nīti, alpa, hrasva; the specials 75 – 94), the iva senses 5.3.96 – 110, and the tadrāja pratyayas 5.3.112 – 118. Forms are those of the Kāśikā
(brain db, texts / kashika)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

MN, JN = {"lex:manuzyanAman"}, {"lex:manuzyanAman", "lex:jAtinAman"}
PUG, VRA, AYU = {"lex:pUga"}, {"lex:vrAta"}, {"lex:AyuDajIvisaNGa"}
VAH = AYU | {"lex:vAhIka"}
NP, PU = "napuṃsaka", "puṃliṅga"
HR = {"taddhitArtha": "hrasva"}
IV = {"taddhitArtha": "iva"}
CASES = [   # (vivakṣā, stem, lexical tags, linga, a form that must be among the readings)
    ({"taddhitArtha": "praSaMsA"}, "paTu", None, NP, "paTurUpam"),                      # 5.3.66
    ({"taddhitArtha": "IzadasamApti"}, "paTu", None, NP, "paTukalpam"),                 # 5.3.67
    ({"taddhitArtha": "IzadasamApti"}, "paTu", None, NP, "paTudeSyam"),
    ({"taddhitArtha": "IzadasamApti"}, "paTu", None, NP, "paTudeSIyam"),
    ({"taddhitArtha": "ajYAta"}, "aSva", None, NP, "aSvakam"),                          # 5.3.70 with 5.3.73
    ({"taddhitArtha": "kutsita"}, "aSva", None, NP, "aSvakam"),                         # 5.3.74
    ({"taddhitArtha": "kutsita", "arthaViSeSa": "saMjYA"}, "SUdra", None, NP, "SUdrakam"),   # 5.3.75
    ({"taddhitArtha": "anukampA"}, "putra", None, NP, "putrakam"),                      # 5.3.76
    ({"taddhitArtha": "nIti"}, "DAna", {"lex:anukampAyukta"}, NP, "DAnakam"),           # 5.3.77
    ({"taddhitArtha": "anukampA"}, "devadatta", MN, NP, "devikam"),                     # 5.3.78 ṭhac, 83 lopa
    ({"taddhitArtha": "anukampA"}, "devadatta", MN, NP, "devadattakam"),                # the ka that stays
    ({"taddhitArtha": "anukampA"}, "yajYadatta", MN, NP, "yajYikam"),
    ({"taddhitArtha": "anukampA"}, "devadatta", MN, NP, "devilam"),                     # 5.3.79 ilac
    ({"taddhitArtha": "anukampA"}, "devadatta", MN, NP, "deviyam"),                     # ghan (iya)
    ({"taddhitArtha": "anukampA"}, "datta", MN, NP, "dattakam"),                        # not bahvac: no ṭhac
    ({"taddhitArtha": "anukampA"}, "vyAGra", JN, NP, "vyAGrakam"),                      # 5.3.81
    ({"taddhitArtha": "anukampA"}, "vyAGrAjina", MN, NP, "vyAGrakam"),                  # 5.3.82
    ({"taddhitArtha": "anukampA"}, "Sevaladatta", MN, NP, "Sevalikam"),                 # 5.3.84
    ({"taddhitArtha": "anukampA"}, "viSAladatta", MN, NP, "viSAlikam"),
    ({"taddhitArtha": "anukampA"}, "aryamadatta", MN, NP, "aryamikam"),
    ({"taddhitArtha": "alpa"}, "tEla", None, NP, "tElakam"),                            # 5.3.85
    ({**HR}, "vfkza", None, NP, "vfkzakam"),                                            # 5.3.86
    ({**HR, "arthaViSeSa": "saMjYA"}, "vaMSa", None, NP, "vaMSakam"),                   # 5.3.87
    ({**HR}, "kuwI", None, NP, "kuwIram"),                                              # 5.3.88
    ({**HR}, "SamI", None, NP, "SamIram"),
    ({**HR}, "SuRqA", None, NP, "SuRqAram"),
    ({**HR}, "kutU", None, NP, "kutupam"),                                              # 5.3.89
    ({**HR}, "kAsU", None, NP, "kAsUtaram"),                                            # 5.3.90
    ({**HR}, "goRI", None, NP, "goRItaram"),
    ({**HR, "arthaViSeSa": "tanutva"}, "vatsa", None, NP, "vatsataram"),                # 5.3.91
    ({**HR, "arthaViSeSa": "tanutva"}, "aSva", None, NP, "aSvataram"),
    ({**HR, "arthaViSeSa": "tanutva"}, "fzaBa", None, NP, "fzaBataram"),
    ({"taddhitArtha": "nirDAraRadvaya"}, "kim", None, PU, "kataraH"),                   # 5.3.92
    ({"taddhitArtha": "nirDAraRadvaya"}, "kim", None, NP, "katarat"),
    ({"taddhitArtha": "nirDAraRadvaya"}, "tad", None, PU, "tataraH"),
    ({"taddhitArtha": "nirDAraRabahu", "arthaViSeSa": "jAtiparipraSna"}, "kim", None, PU, "katamaH"),   # 5.3.93
    ({"taddhitArtha": "nirDAraRadvaya", "arthaViSeSa": "prAcAm"}, "eka", None, PU, "ekataraH"),         # 5.3.94
    ({"taddhitArtha": "nirDAraRabahu", "arthaViSeSa": "prAcAm"}, "eka", None, PU, "ekatamaH"),
    ({"taddhitArtha": "avakzepaRa"}, "aSva", None, NP, "aSvakam"),                      # 5.3.95
    ({**IV, "arthaViSeSa": "pratikfti"}, "aSva", None, NP, "aSvakam"),                  # 5.3.96
    ({**IV, "arthaViSeSa": "saMjYA"}, "aSva", None, NP, "aSvakam"),                     # 5.3.97
    ({**IV, "arthaViSeSa": "saMjYA", "abhiDeya": "manuzya"}, "caYcA", None, "strīliṅga", "caYcA"),              # 5.3.98 lup
    ({**IV, "arthaViSeSa": "pratikfti", "jIvikArTa": "jIvikArTa", "abhiDeya": "apaRya"}, "Siva", None, PU, "SivaH"),   # 5.3.99
    ({**IV, "arthaViSeSa": "pratikfti"}, "devapaTa", None, PU, "devapaTaH"),            # 5.3.100
    ({**IV}, "vasti", None, NP, "vAsteyam"),                                            # 5.3.101
    ({**IV}, "SilA", None, NP, "Sileyam"),                                              # 5.3.102
    ({**IV}, "SAKA", None, NP, "SAKyam"),                                               # 5.3.103
    ({**IV}, "kuSAgra", None, NP, "kuSAgrIyam"),                                        # 5.3.105
    ({**IV}, "SarkarA", None, NP, "SArkaram"),                                          # 5.3.107
    ({**IV}, "aNguli", None, NP, "ANgulikam"),                                          # 5.3.108
    ({**IV}, "ekaSAlA", None, NP, "ekaSAlikam"),                                        # 5.3.109 ṭhac
    ({**IV}, "ekaSAlA", None, NP, "EkaSAlikam"),                                        # ṭhak
    ({**IV}, "karka", None, NP, "kArkIkam"),                                            # 5.3.110
    ({**IV}, "lohita", None, NP, "lOhitIkam"),
    ({}, "lOhaDvaja", PUG, NP, "lOhaDvajyam"),                                          # 5.3.112
    ({}, "kapotapAka", VRA, NP, "kApotapAkyam"),                                        # 5.3.113
    ({}, "kuRqIbfsa", VAH, NP, "kORqIbfsyam"),                                          # 5.3.114
    ({}, "mAlava", VAH, NP, "mAlavyam"),
    ({}, "vfka", AYU, NP, "vArkeRyam"),                                                 # 5.3.115
    ({}, "dAmanI", AYU, NP, "dAmanIyam"),                                               # 5.3.116
    ({}, "Olapi", AYU, NP, "OlapIyam"),
    ({}, "parSu", AYU, NP, "pArSavam"),                                                 # 5.3.117
    ({}, "yODeya", AYU, NP, "yODeyam"),
    ({}, "ABijita", None, NP, "ABijityam"),                                             # 5.3.118
    ({}, "SAlAvata", None, NP, "SAlAvatyam"),
]


def _forms(viv, stem, og, linga):
    return {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, stem_linga=linga if viv.get("abhiDeya") else None, **viv))}


@pytest.mark.parametrize("viv,stem,og,linga,want", CASES, ids=lambda c: None)
def test_forms(viv, stem, og, linga, want):
    got = _forms(viv, stem, og, linga)
    assert want in got, sorted(got)


def test_no_thac_below_three_vowels():
    got = _forms({"taddhitArtha": "anukampA"}, "datta", MN, NP)
    assert "dattikam" not in got and "dattilam" not in got, sorted(got)


def test_stem_without_vahika_tag_gets_no_nyat():
    got = _forms({}, "mAlava", AYU, NP)
    assert "mAlavyam" not in got, sorted(got)


@pytest.mark.xfail(strict=True, reason="7.1.25 adḍ is given only to a list of stems: yad + ḍatarac gives yataram, not yatarat")
def test_yatarat():
    assert "yatarat" in _forms({"taddhitArtha": "nirDAraRadvaya"}, "yad", None, NP)      # 5.3.92
