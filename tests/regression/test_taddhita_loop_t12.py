"""T12 — 5.1.95 – 112: dakṣiṇā of a sacrifice, bhava-vat (the sense frame), what is given / done with it, sampādin, prabhavati (santāpādi, yoga, karman),
prāpta (samaya, ṛtu, kāla), prakṛṣṭa, and prayojana with the specials 5.1.110 – 112."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

K, Y, SM = {"lex:kAla"}, {"lex:yajYAKya"}, {"lex:samAsa"}
CASES = [   # (sense, stem, lexical tags, extra vivakṣā, a form that must be among the readings)
    ("dakziRA", "agnizwoma", Y, {}, "Agnizwomikam"),                  # 5.1.95
    ("kAladIyate", "nizkramaRa", K, {}, "nEzkramaRam"),               # 5.1.96 frame, 5.1.97 (vyuṣṭa → vaiyuṣṭa needs 7.3.3, not real)
    ("kAlatatrakArya", "nitya", K, {}, "nEtyam"),
    ("kAlatatrakArya", "tIrTa", K, {}, "tErTam"),
    ("tenadIyate", "yaTAkaTAcA", None, {}, "yATAkaTAcam"),            # 5.1.98
    ("tenakArya", "hasta", None, {}, "hastyam"),
    ("sampAdin", "karRavezwaka", None, {}, "kArRavezwakikam"),        # 5.1.99
    ("sampAdin", "karmaveza", None, {}, "karmavezyam"),               # 5.1.100
    ("tasmaiPraBavati", "saMtApa", None, {}, "sAntApikam"),           # 5.1.101
    ("tasmaiPraBavati", "yoga", None, {}, "yogyam"),                  # 5.1.102
    ("tasmaiPraBavati", "yoga", None, {}, "yOgikam"),
    ("prApta", "samaya", None, {}, "sAmayikam"),                      # 5.1.104
    ("prApta", "ftu", None, {}, "Artavam"),                # 5.1.105
    ("prApta", "kAla", None, {}, "kAlyam"),                           # 5.1.107
    ("prakfzwa", "kAla", None, {}, "kAlikam"),                        # 5.1.108
    ("prayojana", "indramaha", None, {}, "Endramahikam"),             # 5.1.109
    ("prayojana", "viSAKA", None, {"arthaViSeSa": "manTa"}, "vESAKam"),  # 5.1.110
    ("prayojana", "AzAQA", None, {"arthaViSeSa": "daRqa"}, "AzAQam"),
    ("prayojana", "anupravacana", None, {}, "anupravacanIyam"),       # 5.1.111
    ("prayojana", "fksamApana", SM, {}, "fksamApanIyam"),   # 5.1.112
]


@pytest.mark.xfail(reason="S21: 6.4.144 does not yet drop the ṭi of an-stems (karman + ukaÑ gives kArmaRukam, not kArmukam)", strict=True)
def test_karman_ukan():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("karman", 1, 1, "napuṃsaka", taddhitArtha="tasmaiPraBavati"))}
    assert "kArmukam" in got, sorted(got)      # 5.1.103


@pytest.mark.parametrize("sense,stem,og,extra,want", CASES, ids=lambda c: None)
def test_senses(sense, stem, og, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)


def test_bhavavat_frame_has_no_default():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("mAsa", 1, 1, "napuṃsaka", origin_tags=K, taddhitArtha="kAladIyate"))}
    assert "mAsikam" not in got, sorted(got)
