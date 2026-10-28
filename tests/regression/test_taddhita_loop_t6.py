"""T6 — 4.4.75 – 109: the yat group (prāg hitād yat, 4.4.75): vahati, vidhyati, labdhā, gata, dṛśya, saṃyukta, nāvādi, anapeta, nirmita, sādhu, śayita …
a sense opens a frame, yat (4.4.75) attaches to the stems the opener admits, the specials (ḍhak, kha, aṇ, ṇa, ṇya, khañ, ṭhak, ṭhañ, ḍhañ, ya) are apavādas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

SJ = {"arthaViSeSa": "saMjYA"}
CASES = [   # (stem, lexical tags, sense, extra vivakṣā, form that must be one of the readings)
    ("raTa", None, "vahati", {}, "raTyaH"),                      # 4.4.76
    ("yuga", None, "vahati", {}, "yugyaH"),
    ("Dur", None, "vahati", {}, "DuryaH"),                       # 4.4.77 yat
    ("Dur", None, "vahati", {}, "DOreyaH"),                      # ḍhak
    ("sarvaDurA", None, "vahati", {}, "sarvaDurIRaH"),           # 4.4.78 kha
    ("ekaDurA", None, "vahati", {}, "ekaDurIRaH"),               # 4.4.79
    ("Sakawa", None, "vahati", {}, "SAkawaH"),                   # 4.4.80
    ("hala", None, "vahati", {}, "hAlikaH"),                     # 4.4.81
    ("janI", None, "vahati", SJ, "janyaH"),                      # 4.4.82
    ("Uru", None, "viDyati", {}, "UravyaH"),                     # 4.4.83
    ("Dana", None, "labDA", {}, "DanyaH"),                       # 4.4.84
    ("anna", None, "labDA", {}, "AnnaH"),                        # 4.4.85 ṇa
    ("vaSa", None, "gata", {}, "vaSyaH"),                        # 4.4.86
    ("pada", None, "dfSya", {}, "padyaH"),                       # 4.4.87
    ("mUla", None, "Abarhi", {}, "mUlyaH"),                      # 4.4.88
    ("gfhapati", None, "saMyukta", SJ, "gArhapatyaH"),           # 4.4.90 ñya
    ("nO", None, "tArya", SJ, "nAvyaH"),                         # 4.4.91
    ("vayas", None, "tulya", SJ, "vayasyaH"),
    ("tulA", None, "sammita", SJ, "tulyaH"),
    ("Darma", None, "anapeta", {}, "DarmyaH"),                   # 4.4.92
    ("arTa", None, "anapeta", {}, "arTyaH"),
    ("Candas", None, "nirmita", SJ, "CandasyaH"),                # 4.4.93
    ("uras", None, "nirmita", {}, "OrasaH"),                     # 4.4.94 aṇ ca
    ("uras", None, "nirmita", {}, "urasyaH"),
    ("pratijana", None, "sADu", SJ, "prAtijanInaH"),             # 4.4.99 khañ
    ("Bakta", None, "sADu", SJ, "BAktaH"),                       # 4.4.100
    ("parizad", None, "sADu", SJ, "pArizadyaH"),                 # 4.4.101
    ("kaTA", None, "sADu", SJ, "kATikaH"),                       # 4.4.102
    ("guqa", None, "sADu", SJ, "gOqikaH"),                       # 4.4.103
    ("atiTi", None, "sADu", SJ, "AtiTeyaH"),                     # 4.4.104 ḍhañ
    ("saBA", None, "sADu", SJ, "saByaH"),                        # 4.4.105
    ("sodara", None, "Sayita", SJ, "sodaryaH"),                  # 4.4.109
]


@pytest.mark.parametrize("stem,og,sense,extra,want", CASES, ids=lambda c: None)
def test_sense(stem, og, sense, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "pulliṅga", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)
