"""T9 — 5.1.18 – 37: the ārhīya group. tena krītam (5.1.37) opens the sense; ṭhañ (5.1.18) is the default, ṭhak (5.1.19) for what is not gopucchādi / saṃkhyā /
parimāṇa; 5.1.20 – 27 are its apavādas; 5.1.28 – 31 take the pratyaya away (luk) after adhyardhapūrva / dvigu stems (S27: flat lexical compounds)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

DV = {"lex:aDyarDapUrvadvigu"}
CASES = [   # (stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("pARi", None, {}, "pARikam"),                                  # 5.1.19 ṭhak
    ("gopucCa", {"lex:gopucCAdi"}, {}, "gOpucCikam"),               # not ṭhak: 5.1.18 ṭhañ
    ("saptati", {"lex:saMKyA"}, {}, "sAptatikam"),                  # saṃkhyā ending in ti: ṭhañ
    ("prasTa", {"lex:parimARa"}, {}, "prAsTikam"),                 # parimāṇa: ṭhañ
    ("nizka", None, {}, "nEzkikam"),                                # 5.1.20
    ("mAza", {"lex:parimARa"}, {}, "mAzikam"),                      # 5.1.20 over 5.1.18 for a parimāṇa
    ("Sata", {"lex:saMKyA"}, {}, "Satikam"),                        # 5.1.21 ṭhan
    ("Sata", {"lex:saMKyA"}, {}, "Satyam"),                         # 5.1.21 yat
    ("paYcan", {"lex:saMKyA"}, {}, "paYcakam"),                     # 5.1.22
    ("tAvat", {"lex:saMKyA"}, {}, "tAvatikam"),                     # 5.1.23 iṭ
    ("tAvat", {"lex:saMKyA"}, {}, "tAvatkam"),
    ("viMSati", {"lex:saMKyA"}, {}, "viMSakam"),                    # 5.1.24
    ("viMSati", {"lex:saMKyA"}, {"arthaViSeSa": "saMjYA"}, "viMSatikam"),
    ("kaMsa", None, {}, "kaMsikam"),                                 # 5.1.25 ṭiṭhan (ṭhan is not ñit/ṇit: no vṛddhi)
    ("SUrpa", None, {}, "SOrpam"),                                  # 5.1.26 añ
    ("SUrpa", {"lex:parimARa"}, {}, "SOrpikam"),                    # or ṭhañ
    ("SatamAna", None, {}, "SAtamAnam"),                            # 5.1.27 aṇ
    ("sahasra", None, {}, "sAhasram"),
    ("aDyarDakaMsa", DV, {}, "aDyarDakaMsam"),                      # 5.1.28 luk
    ("dvikaMsa", DV, {}, "dvikaMsam"),
    ("dvikArzApaRa", DV, {}, "dvikArzApaRam"),                      # 5.1.29 vibhāṣā luk
    ("dvisahasra", DV, {}, "dvisahasram"),
    ("dviSARa", DV | {"lex:dvitripUrva"}, {}, "dviSARyam"),         # 5.1.36 yat
    ("dviSARa", DV | {"lex:dvitripUrva"}, {}, "dviSARam"),          # luk
    ("aDyarDaSARa", DV, {}, "aDyarDaSARyam"),                       # 5.1.35
    ("aDyarDaviMSatika", DV, {}, "aDyarDaviMSatikInam"),            # 5.1.32 kha
]


@pytest.mark.parametrize("stem,og,extra,want", CASES, ids=lambda c: None)
def test_krita(stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha="krIta", **extra))}
    assert want in got, sorted(got)
