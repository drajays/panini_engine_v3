"""T11 — 5.1.64 – 94: the ṭhañ group continued. The arhati specials (5.1.64 – 71), what he does / where he goes (72 – 77), and the kāla senses (79 – 94):
nirvṛtta, adhīṣṭa / bhṛta / bhūta / bhāvī, parijayya …, brahmacarya, with the specials 5.1.81 – 89 for māsa, dvigu, samā, rātri, varṣa."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

K, KD = {"lex:kAla"}, {"lex:kAla", "lex:dvigu"}
V, AV, CV = {"arthaViSeSa": "vayas"}, {"arthaViSeSa": "avayas"}, {"arthaViSeSa": "cittavat"}
AB = {"bhavizyat": "aBavizyat"}      # 7.3.16 abhaviṣyati
CASES = [   # (sense, stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("arhati", "Ceda", None, {"nityatA": "nitya"}, "CEdikam"),         # 5.1.64
    ("arhati", "Beda", None, {"nityatA": "nitya"}, "BEdikam"),
    ("arhati", "daRqa", None, {}, "daRqyam"),                           # 5.1.66 yat
    ("arhati", "musala", None, {}, "musalyam"),
    ("arhati", "pAtra", None, {}, "pAtriyam"),                          # 5.1.68
    ("arhati", "pAtra", None, {}, "pAtryam"),
    ("arhati", "kaqaNkara", None, {}, "kaqaNkarIyam"),                  # 5.1.69
    ("arhati", "kaqaNkara", None, {}, "kaqaNkaryam"),
    ("arhati", "dakziRA", None, {}, "dakziRIyam"),
    ("arhati", "sTAlIbila", None, {}, "sTAlIbilIyam"),                  # 5.1.70
    ("arhati", "yajYa", None, {}, "yajYiyam"),                          # 5.1.71
    ("arhati", "ftvij", None, {}, "ArtvijInam"),
    ("vartayati", "pArAyaRa", None, {}, "pArAyaRikam"),                 # 5.1.72
    ("vartayati", "turAyaRa", None, {}, "tOrAyaRikam"),
    ("vartayati", "cAndrAyaRa", None, {}, "cAndrAyaRikam"),
    ("saMSayApanna", "saMSaya", None, {}, "sAMSayikam"),                # 5.1.73
    ("yojanagacCati", "yojana", None, {}, "yOjanikam"),                 # 5.1.74
    ("gacCati", "paTin", None, {}, "paTikam"),                          # 5.1.75
    ("uttarapaTa", "uttarapaTa", None, {}, "OttarapaTikam"),            # 5.1.77
    ("kAlanirvftta", "mAsa", K, {}, "mAsikam"),                         # 5.1.79
    ("kAlanirvftta", "saMvatsara", K, {}, "sAMvatsarikam"),
    ("kAlAdhIzwa", "mAsa", K, {}, "mAsikam"),                           # 5.1.80
    ("kAlaBfta", "saMvatsara", K, {}, "sAMvatsarikam"),
    ("kAlaBAvI", "mAsa", K, {}, "mAsikam"),
    ("kAlaBUta", "mAsa", K, V, "mAsyam"),                               # 5.1.81
    ("kAlaBUta", "mAsa", K, V, "mAsInam"),
    ("kAlaBUta", "mAsa", K, AV, "mAsikam"),                             # avayasi: the default
    ("kAlaBUta", "dvimAsa", KD, V, "dvimAsyam"),                        # 5.1.82
    ("kAlaBUta", "zaRmAsa", KD, V, "zARmAsyam"),                        # 5.1.83
    ("kAlaBUta", "zaRmAsa", KD, V, "zARmAsikam"),
    ("kAlaBUta", "zaRmAsa", KD, AV, "zaRmAsikam"),                      # 5.1.84
    ("kAlaBUta", "zaRmAsa", KD, AV, "zARmAsyam"),
    ("kAlAdhIzwa", "samA", K, {}, "samInam"),                           # 5.1.85
    ("kAlAdhIzwa", "dvisamA", KD, {}, "dvisamInam"),                    # 5.1.86
    ("kAlAdhIzwa", "dvisamA", KD, {}, "dvEsamikam"),
    ("kAlanirvftta", "dvirAtri", KD, {}, "dvirAtrIRam"),                # 5.1.87
    ("kAlanirvftta", "dvirAtri", KD, {}, "dvErAtrikam"),
    ("kAlaBUta", "dvivarza", KD, V | AB, "dvivarzIRam"),                     # 5.1.88
    ("kAlaBUta", "dvivarza", KD, V | AB, "dvivArzikam"),
    ("kAlaBUta", "dvivarza", KD, V | AB, "dvivarzam"),                       # luk
    ("kAlaBUta", "dvivarza", KD, CV | AB, "dvivarzam"),                      # 5.1.89 nityam
    ("kAlaparijayya", "mAsa", K, {}, "mAsikam"),                        # 5.1.93
    ("kAlalaBya", "mAsa", K, {}, "mAsikam"),
    ("kAlakArya", "mAsa", K, {}, "mAsikam"),
    ("kAlasukara", "mAsa", K, {}, "mAsikam"),
    ("kAlabrahmacarya", "mAsa", K, {}, "mAsikam"),                      # 5.1.94
]


@pytest.mark.parametrize("sense,stem,og,extra,want", CASES, ids=lambda c: None)
def test_senses(sense, stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)


def test_cittavat_only_luk():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("dvivarza", 1, 1, "napuṃsaka", origin_tags=KD, taddhitArtha="kAlaBUta", arthaViSeSa="cittavat", bhavizyat="aBavizyat"))}
    assert "dvivArzikam" not in got and "dvivarzIRam" not in got, sorted(got)
