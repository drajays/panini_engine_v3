"""T4 — the rest of 4.3 that the loop can do: prabhavati / gacchati / abhiniṣkrāmati senses, tavaka-mamaka (4.3.3), the avayava sense (4.3.135) and the
vikāra specials 4.3.136–165 (aṇ, añ, ṣuk, ṭlañ, mayaṭ, kan, vuñ, ḍhañ, yat, vaya)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

CASES = [   # (stem, lexical tags, sense, extra vivakṣā, form that must be one of the readings)
    ("himavat", None, "praBavati", {}, "hEmavataH"),
    ("vidUra", None, "praBavati", {}, "vEdUryaH"),                            # 4.3.84 ñya
    ("mathurA", None, "gacCatiPaTiDUta", {}, "mAthuraH"),                      # 4.3.85
    ("mathurA", None, "abhinizkrAmati", {}, "mAthuraH"),                       # 4.3.86
    ("SiSukranda", None, "granTa", {}, "SiSukrandIyaH"),                      # 4.3.88 cha
    ("yuzmad", None, "Seza", {"ekavacana": "ekavacana"}, "tAvakInaH"),        # 4.3.3 tavaka + khañ
    ("yuzmad", None, "Seza", {"ekavacana": "ekavacana"}, "tAvakaH"),          # + aṇ (4.3.1 anyatarasyām leaves it)
    ("asmad", None, "Seza", {"ekavacana": "ekavacana"}, "mAmakInaH"),
    ("yuzmad", None, "Seza", {}, "yOzmAkIRaH"),                               # 4.3.2 without the ekavacana
    ("bilva", None, "vikAra", {}, "bElvaH"),                                  # 4.3.136
    ("tarku", None, "vikAra", {}, "tArkavaH"),                                # 4.3.137 beats añ
    ("trapu", None, "vikAra", {}, "trApuzaH"),                                # 4.3.138 ṣuk
    ("jatu", None, "vikAra", {}, "jAtuzaH"),
    ("dru", None, "vikAra", {}, "dravyaH"),                                   # 4.3.161 yat
    ("palASa", None, "vikAra", {}, "pAlASaH"),                                # 4.3.141
    ("SamI", None, "vikAra", {}, "SAmIlaH"),                                  # 4.3.142 ṭlañ
    ("aSman", None, "vikAra", {}, "aSmamayaH"),                               # 4.3.143 mayaṭ (vā); 8.2.7 nalopa — Kāśikā aśmamayam
    ("aSman", None, "vikAra", {}, "ASmanaH"),
    ("go", None, "vikAra", {"vikAraBeda": "purIza"}, "gomayaH"),              # 4.3.145
    ("pizwa", None, "vikAra", {}, "pizwamayaH"),                              # 4.3.146
    ("pizwa", None, "vikAra", {"vikAraBeda": "saMjYA"}, "pizwakaH"),          # 4.3.147 kan
    ("vrIhi", None, "vikAra", {"vikAraBeda": "puroqASa"}, "vrIhimayaH"),      # 4.3.148
    ("vrIhi", None, "vikAra", {}, "vrEhaH"),
    ("tila", None, "vikAra", {}, "tilamayaH"),         # 4.3.149
    ("tAla", None, "vikAra", {}, "tAlaH"),                                    # 4.3.152
    ("rajata", None, "vikAra", {}, "rAjataH"),                                # 4.3.154
    ("kapota", {"lex:prANi"}, "avayava", {}, "kApotaH"),                      # 4.3.135 + 154
    ("uzwra", None, "vikAra", {}, "OzwrakaH"),                                # 4.3.157 vuñ → aka (7.1.1)
    ("umA", None, "vikAra", {}, "OmakaH"),                                    # 4.3.158
    ("eRI", None, "vikAra", {}, "EReyaH"),                                    # 4.3.159 ḍhañ
    ("dru", None, "vikAra", {"vikAraBeda": "mAna"}, "druvayaH"),              # 4.3.162
    ("plakza", None, "vikAra", {"vikAraBeda": "Pala"}, "plAkzaH"),            # 4.3.164
    ("jambU", None, "vikAra", {"vikAraBeda": "Pala"}, "jAmbavaH"),            # 4.3.165
]


@pytest.mark.parametrize("stem,og,sense,extra,want", CASES, ids=lambda c: None)
def test_sense(stem, og, sense, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "pulliṅga", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)


def test_himavat_feminine():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("himavat", 1, 1, "strīliṅga", taddhitArtha="praBavati"))}
    assert "hEmavatI" in got, sorted(got)
