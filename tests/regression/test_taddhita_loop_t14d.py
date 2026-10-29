"""T14d — 5.4.81 – 159: the samāsānta pratyayas (ac, ṭac, ṣac, ṣa, ap, ic, kap) of a compound given as one Term (S62: its kind is a lex: tag, its last
member is read off the letters), in the frame 5.4.68 opens from the vivakṣā ``taddhitArtha=samAsAnta``, and the barring sūtras 5.4.155 – 159 of kap."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

N, P = "napuṃsaka", "pulliṅga"
SJ, DA, KV = {"arthaViSeSa": "saMjYA"}, {"arthaViSeSa": "dAru"}, {"arthaViSeSa": "karmavyatihAra"}
CASES = [   # (stem, lex: tags, extra vivakṣā, liṅga, a form that must be among the readings)
    ("anurahas", {"samAsa"}, {}, N, "anurahasam"),                                   # 5.4.81
    ("pratyuras", {"avyayIBAva"}, {}, N, "pratyurasam"),                             # 82
    ("dvyaNguli", {"tatpuruza", "saMKyAvyayAdi"}, {}, N, "dvyaNgulam"),             # 86
    ("sarvarAtri", {"tatpuruza"}, {}, P, "sarvarAtraH"),                             # 87
    ("vibudhasaKi", {"tatpuruza"}, {}, P, "vibudhasaKaH"),                           # 91
    ("aSvoras", {"tatpuruza", "agrAKyA"}, {}, N, "aSvorasam"),                       # 93
    ("paramago", {"tatpuruza"}, {}, P, "paramagavaH"),                               # 92
    ("mahAnas", {"tatpuruza"}, SJ, N, "mahAnasam"),                                  # 94
    ("lohitAyas", {"tatpuruza"}, SJ, N, "lohitAyasam"),
    ("uttarasakTi", {"tatpuruza", "uttaramfgapUrva"}, {}, N, "uttarasakTam"),        # 98
    ("paYcanO", {"dvigu"}, {}, N, "paYcanAvam"),                                     # 99
    ("arDanO", {"tatpuruza"}, {}, N, "arDanAvam"),                                   # 100
    ("arDaKArI", {"tatpuruza"}, {}, N, "arDaKAram"),                                 # 101
    ("dvyaYjali", {"dvigu"}, {}, N, "dvyaYjalam"),                                   # 102
    ("vAkwvac", {"dvandva", "samAhAra"}, {}, N, "vAkwvacam"),                        # 106
    ("samiDdfzad", {"dvandva", "samAhAra"}, {}, N, "samiddfzadam"),
    ("upazarad", {"avyayIBAva"}, {}, N, "upazaradam"),                               # 107
    ("upapOrRamAsI", {"avyayIBAva"}, {}, N, "upapOrRamAsam"),                        # 110
    ("upAgrahAyaRI", {"avyayIBAva"}, {}, N, "upAgrahAyaRam"),
    ("upasamiD", {"avyayIBAva"}, {}, N, "upasamiDam"),                               # 111
    ("upagiri", {"avyayIBAva"}, {}, N, "upagiram"),                                  # 112
    ("upakuwumba", {"avyayIBAva", "napuMsakAnta"}, {}, N, "upakuwumbam"),            # 109
    ("kamalAkzi", {"bahuvrIhi", "svAfga"}, {}, P, "kamalAkzaH"),                     # 113
    ("paYcANguli", {"bahuvrIhi"}, DA, N, "paYcANgulam"),                             # 114
    ("kalyARIpaYcamI", {"bahuvrIhi", "pUraRI"}, {}, P, "kalyARIpaYcamaH"),           # 116
    ("susakTi", {"bahuvrIhi"}, {}, P, "susakTaH"),                                   # 121
    ("kezAkeza", {"bahuvrIhi"}, KV, N, "kezAkezi"),                                  # 127
    ("bahusarpiz", {"bahuvrIhi"}, {}, P, "bahusarpizkaH"),                               # 151
    ("bahukartf", {"bahuvrIhi"}, {}, P, "bahukartfkaH"),                             # 153
    ("bahuKawva", {"bahuvrIhi"}, {}, P, "bahuKawvakaH"),                             # 154
    ("bahuKawva", {"bahuvrIhi"}, {}, P, "bahuKawvaH"),
]
BARRED = [  # kap does not follow: 155 in a name, 156 Iyas, 159 nāḍī of the body
    ("bahuKawva", {"bahuvrIhi"}, SJ, P, "bahuKawvakaH"),
    ("bahugarIyas", {"bahuvrIhi"}, {}, P, "bahugarIyaskaH"),
    ("bahunADI", {"bahuvrIhi", "svAfga"}, {}, P, "bahunADIkaH"),
    ("bahuBrAtf", {"bahuvrIhi"}, {"arthaViSeSa": "vandita"}, P, "bahuBrAtfkaH"),       # 157
]
AN_STEMS = [   # 6.4.144 drops the ṭi of an-stems (S21 closed)
    ("prADvan", {"samAsa"}, {}, P, "prADvaH"),                                       # 85
    ("paramarAjan", {"tatpuruza"}, {}, P, "paramarAjaH"),                            # 91
    ("grAmatakzan", {"tatpuruza"}, {}, P, "grAmatakzaH"),                            # 95
    ("dvimUrDan", {"bahuvrIhi"}, {}, P, "dvimUrDaH"),                                # 115
    ("surAzwrabrahman", {"tatpuruza"}, {"arthaViSeSa": "jAnapadAKyA"}, P, "surAzwrabrahmaH"),   # 104
    ("kubrahman", {"tatpuruza"}, {}, P, "kubrahmaH"),                                # 105
    ("uparAjan", {"avyayIBAva"}, {}, N, "uparAjam"),                                 # 108
    ("antarloman", {"bahuvrIhi"}, {}, P, "antarlomaH"),                              # 117
    ("atiSvan", {"tatpuruza"}, {}, P, "atiSvaH"),                                    # 96
]


def _forms(stem, tags, extra, linga):
    og = {"lex:" + t for t in tags}
    return {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, taddhitArtha="samAsAnta", **extra))}


@pytest.mark.parametrize("stem,tags,extra,linga,want", CASES, ids=lambda c: None)
def test_samasanta(stem, tags, extra, linga, want):
    got = _forms(stem, tags, extra, linga)
    assert want in got, sorted(got)


@pytest.mark.parametrize("stem,tags,extra,linga,nowant", BARRED, ids=lambda c: None)
def test_kap_barred(stem, tags, extra, linga, nowant):
    got = _forms(stem, tags, extra, linga)
    assert nowant not in got, sorted(got)


@pytest.mark.parametrize("stem,tags,extra,linga,want", AN_STEMS, ids=lambda c: None)
def test_an_stems(stem, tags, extra, linga, want):
    got = _forms(stem, tags, extra, linga)
    assert want in got, sorted(got)
