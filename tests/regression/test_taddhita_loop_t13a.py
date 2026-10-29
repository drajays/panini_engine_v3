"""T13a — 5.2.1 – 45: the senses each sūtra names itself (khañ in the field of grains, the specials 5.2.2 – 4, khá of darśana / vyāpnoti / gāmī …,
kuṇap / jāhac, aṇ / itac, pramāṇa and parimāṇa pratyayas, tayap / ayac, the daśānta ḍa).  The xfail rows are real gaps named in their reason."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

N, S = "napuṃsaka", "strīliṅga"
D, SM, Q = {"lex:dhAnya"}, {"lex:samAsa"}, {"lex:saMKyA"}
CASES = [   # (sense, stem, lexical tags, liṅga, a form that must be among the readings)
    ("kzetra", "mudga", D, N, "mOdgInam"),                       # 5.2.1
    ("kzetra", "vrIhi", D, N, "vrEheyam"),                       # 5.2.2
    ("kzetra", "SAli", D, N, "SAleyam"),
    ("kzetra", "yava", D, N, "yavyam"),                          # 5.2.3
    ("kzetra", "zazwika", D, N, "zazwikyam"),
    ("kzetra", "tila", D, N, "tilyam"),                          # 5.2.4 vibhāṣā
    ("kzetra", "tila", D, N, "tElInam"),
    ("kzetra", "mAza", D, N, "mAzIRam"),
    ("darSana", "yaTAmuKa", None, N, "yaTAmuKInam"),            # 5.2.6
    ("darSana", "saMmuKa", None, N, "sammuKInam"),
    ("vyApnoti", "sarvapaTin", SM, N, "sarvapaTInam"),          # 5.2.7
    ("vyApnoti", "sarvapAtra", SM, N, "sarvapAtrIRam"),
    ("vyApnoti", "sarvapatra", SM, N, "sarvapatrIRam"),
    ("vyApnoti", "sarvANga", SM, N, "sarvANgIRam"),
    ("prApnoti", "Aprapada", None, N, "AprapadInam"),           # 5.2.8
    ("baddhA", "anupada", None, N, "anupadInam"),               # 5.2.9
    ("neya", "ayAnaya", None, N, "ayAnayInam"),
    ("anuBavati", "parovara", None, N, "parovarIRam"),          # 5.2.10
    ("anuBavati", "putrapOtra", None, N, "putrapOtrIRam"),
    ("gAmI", "avArapAra", None, N, "avArapArIRam"),             # 5.2.11
    ("gAmI", "atyanta", None, N, "atyantInam"),
    ("gAmI", "anukAma", None, N, "anukAmInam"),
    ("alaMgAmI", "anugu", None, N, "anugavInam"),               # 5.2.15
    ("alaMgAmI", "aDvan", None, N, "aDvanInam"),                # 5.2.16 (the n stays by 6.4.168 / 6.4.169 as well)
    ("alaMgAmI", "aDvan", None, N, "aDvanyam"),
    ("alaMgAmI", "aByamitra", None, N, "aByamitrIyam"),         # 5.2.17
    ("alaMgAmI", "aByamitra", None, N, "aByamitryam"),
    ("alaMgAmI", "aByamitra", None, N, "aByamitrIRam"),
    ("BUtapUrva", "gozWa", None, N, "gOzWInam"),                # 5.2.18
    ("ekAhagama", "aSva", None, N, "ASvInam"),                  # 5.2.19
    ("vrAtajIvati", "vrAta", None, N, "vrAtInam"),              # 5.2.21
    ("pAka", "pIlu", None, N, "pIlukuRam"),                     # 5.2.24
    ("saMjAta", "tArakA", None, N, "tArakitam"),                # 5.2.36
    ("pramANa", "Uru", None, N, "Urudvayasam"),                 # 5.2.37
    ("pramANa", "Uru", None, N, "UrudaGnam"),
    ("pramANa", "Uru", None, N, "UrumAtram"),
    ("pramANa", "puruza", None, N, "pOruzam"),                  # 5.2.38
    ("pramANa", "puruza", None, N, "puruzadvayasam"),
    ("pramANa", "hastin", None, N, "hAstinam"),
    ("pramANa", "hastin", None, N, "hastimAtram"),
    ("saMKyAparimARa", "kim", None, N, "kati"),                 # 5.2.41
    ("saMKyAvayava", "paYcan", Q, N, "paYcatayam"),             # 5.2.42
    ("saMKyAvayava", "dvi", Q, N, "dvitayam"),                  # 5.2.43
    ("saMKyAvayava", "dvi", Q, N, "dvayam"),
    ("saMKyAvayava", "tri", Q, N, "trayam"),
    ("saMKyAvayava", "uBa", None, N, "uBayam"),                 # 5.2.44
    ("aDika", "ekAdaSan", Q, N, "ekAdaSam"),                    # 5.2.45
    ("sarvacarmakfta", "sarvacarman", None, N, "sarvacarmIRam"),                                 # 5.2.5
    ("vyApnoti", "sarvakarman", SM, N, "sarvakarmIRam"),                                         # 5.2.7
    ("karmaGawa", "karman", None, N, "karmaWam"),                                                # 5.2.35
]
GAPS = [    # the pratyaya is the sūtra's; the form waits for another sūtra
    ("Bakzayati", "sarvAnna", None, N, "sarvAnnInam", "the compound is one Term, so 8.4.1 turns its second n into ṇ across the member boundary (S30 kind)"),   # 5.2.9
    ("mUla", "pakza", None, S, "pakzatiH", "the a of pakza is dropped before ti and ṣ + t becomes ṣṭ (pakzwiH): 6.4.148 reads ti as an i-initial pratyaya"),   # 5.2.25
    ("parimARa", "yad", None, N, "yAvat", "6.3.91 (ā sarvanāmnaḥ) is not real"),                     # 5.2.39
    ("parimARa", "tad", None, N, "tAvat", "6.3.91 is not real"),
    ("parimARa", "etad", None, N, "etAvat", "6.3.91 is not real"),
    ("parimARa", "kim", None, N, "kiyat", "6.3.90 (idaṅkimor īśkī) and 7.1.2 gha → iy are not real for this chain"),   # 5.2.40
    ("parimARa", "idam", None, N, "iyat", "6.3.90 is not real"),
]


def _forms(sense, stem, og, linga):
    return {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, taddhitArtha=sense))}


@pytest.mark.parametrize("sense,stem,og,linga,want", CASES, ids=lambda c: None)
def test_senses(sense, stem, og, linga, want):
    got = _forms(sense, stem, og, linga)
    assert want in got, sorted(got)


@pytest.mark.parametrize("sense,stem,og,linga,want,why", [pytest.param(*g, marks=pytest.mark.xfail(reason=g[-1], strict=True)) for g in GAPS], ids=lambda c: None)
def test_known_gaps(sense, stem, og, linga, want, why):
    assert want in _forms(sense, stem, og, linga)
