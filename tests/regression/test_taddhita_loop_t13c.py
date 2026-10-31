"""T13c — 5.2.94 – 140: the matup group (tadasyāstyasminniti). 5.2.94 opens the sense frame (vivakṣā ``taddhitArtha=astyasya``) with matup as the default;
5.2.95 – 140 are its apavādas (lac, ilac, ṇa, vini, aṇ, ura, ra, ma, va, valac, ini …). A vā special stands aside and leaves matup; the generic 5.2.115 – 117 do not return."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

PS, SM, ASM = {"lex:prANisTa"}, {"lex:samAsa"}, {"lex:samAsa"}
M = {}
CASES = [   # (stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("UrRA", None, M, "UrRAyuH"),                                         # 5.2.123 yus is sit: 1.4.16 pada, so 6.4.148 does not drop the ā (Art. 25 work)
    ("go", None, M, "gomAn"),                                             # 5.2.94
    ("Dana", None, M, "DanavAn"),                                         # + 8.2.9 (S44)
    ("rasa", None, M, "rasavAn"),                                         # 5.2.95 niyama
    ("cUqA", PS, M, "cUqAlaH"),                                           # 5.2.96
    ("cUqA", PS, M, "cUqAvAn"),
    ("siDma", None, M, "siDmalaH"),                                       # 5.2.97
    ("siDma", None, M, "siDmavAn"),
    ("vatsa", None, {"arthaViSeSa": "kAma"}, "vatsalaH"),                 # 5.2.98
    ("aMsa", None, {"arthaViSeSa": "bala"}, "aMsalaH"),
    ("Pena", None, M, "PenilaH"),                                         # 5.2.99
    ("Pena", None, M, "PenalaH"),
    ("Pena", None, M, "PenavAn"),
    ("baBru", None, M, "baBruSaH"),                                       # 5.2.100
    ("kadru", None, M, "kadruRaH"),
    ("picCa", None, M, "picCilaH"),
    ("prajYA", None, M, "prAjYaH"),                                       # 5.2.101
    ("SraddDA", None, M, "SrAddDaH"),
    ("prajYA", None, M, "prajYAvAn"),
    ("tapas", None, M, "tapasvI"),                                        # 5.2.102
    ("sahasra", None, M, "sahasrI"),
    ("tapas", None, M, "tApasaH"),                                        # 5.2.103
    ("sikatA", None, {}, "sEkataH"),                                      # 5.2.104
    ("sikatA", None, {"arthaViSeSa": "deSa"}, "sikatilaH"),               # 5.2.105
    ("sikatA", None, {"arthaViSeSa": "deSa"}, "sikatAH"),
    ("sikatA", None, {"arthaViSeSa": "deSa"}, "sikatAvAn"),
    ("danta", None, {"arthaViSeSa": "unnata"}, "danturaH"),               # 5.2.106
    ("maDu", None, M, "maDuraH"),                                         # 5.2.107
    ("Uza", None, M, "UzaraH"),
    ("dyu", None, M, "dyumaH"),                                           # 5.2.108
    ("dru", None, M, "drumaH"),
    ("keSa", None, M, "keSavaH"),                                         # 5.2.109
    ("keSa", None, M, "keSavAn"),
    ("ajaga", None, {"arthaViSeSa": "saMjYA"}, "ajagavaH"),               # 5.2.110
    ("kARqa", None, M, "kARqIraH"),                                       # 5.2.111
    ("aRqa", None, M, "aRqIraH"),
    ("rajas", None, M, "rajasvalaH"),                                     # 5.2.112
    ("parizad", None, M, "parizadvalaH"),
    ("daRqa", None, M, "daRqI"),                                          # 5.2.115
    ("daRqa", None, M, "daRqikaH"),
    ("daRqa", None, M, "daRqavAn"),
    ("mAyA", None, M, "mAyI"),                                            # 5.2.116
    ("udara", None, M, "udarilaH"),                                       # 5.2.117
    ("udara", None, M, "udarI"),
    ("udara", None, M, "udarikaH"),
    ("ekaniSka", ASM, M, "EkaniSkikaH"),                                  # 5.2.118
    ("goniSka", ASM, M, "gOniSkikaH"),
    ("SataniSka", ASM, M, "SAtaniSkikaH"),                                # 5.2.119
    ("rUpa", None, {"arthaViSeSa": "Ahata"}, "rUpyaH"),                   # 5.2.120
    ("rUpa", None, {"arthaViSeSa": "praSaMsA"}, "rUpyaH"),
    ("yaSas", None, M, "yaSasvI"),                                        # 5.2.121
    ("mAyA", None, M, "mAyAvI"),
    ("vAc", None, {"arthaViSeSa": "bahuBAzin"}, "vAcAlaH"),               # 5.2.125
    ("vAc", None, {"arthaViSeSa": "bahuBAzin"}, "vAcAtaH"),
    ("arSas", None, M, "arSasaH"),                                        # 5.2.127
    ("kuzWa", PS, {"arthaViSeSa": "upatApa"}, "kuzWI"),                   # 5.2.128
    ("paYcama", None, {"arthaViSeSa": "vayas"}, "paYcamI"),               # 5.2.130
    ("suKa", None, M, "suKI"),                                            # 5.2.131
    ("hasta", None, {"arthaViSeSa": "jAti"}, "hastI"),                    # 5.2.133
    ("varRa", None, {"arthaViSeSa": "brahmacAri"}, "varRI"),              # 5.2.134
    ("puzkara", None, {"arthaViSeSa": "deSa"}, "puzkarI"),                # 5.2.135
    ("brAhmaRaDarma", SM, M, "brAhmaRaDarmI"),                            # 5.2.132
    ("sIma", None, {"arthaViSeSa": "saMjYA"}, "sImI"),                    # 5.2.137
    ("bala", None, M, "balI"),                                            # 5.2.136
    ("bala", None, M, "balavAn"),
    ("tundi", None, M, "tundiBaH"),                                       # 5.2.139
    ("ahaM", None, M, "ahaMyuH"),                                         # 5.2.140
    ("SuBaM", None, M, "SuBaMyuH"),
    ("SaM", None, M, "SaMyuH"),                                           # 5.2.138
    ("kaM", None, M, "kaMyuH"),
]


@pytest.mark.parametrize("stem,og,extra,want", CASES, ids=lambda c: None)
def test_senses(stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "puMliNga", origin_tags=og, taddhitArtha="astyasya", **extra))}
    assert want in got, sorted(got)


XFAIL = [   # (stem, extra, want, cause)
    ("danta", {"arthaViSeSa": "saMjYA"}, "dantAvalaH", "5.2.113: the long ā of dantāvala (dīrgha before valac) is not modelled"),
]


@pytest.mark.parametrize("stem,extra,want,why", XFAIL, ids=lambda c: None)
def test_known_gaps(stem, extra, want, why):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "puMliNga", taddhitArtha="astyasya", **extra))}
    if want in got:
        pytest.fail(f"now derived — move to CASES: {want}")
    pytest.xfail(why)


def test_special_stands_aside_barring_generic():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("Pena", 1, 1, "puMliNga", taddhitArtha="astyasya"))}
    assert "PenI" not in got and "PenikaH" not in got, sorted(got)      # phena: only ilac, lac, matup
