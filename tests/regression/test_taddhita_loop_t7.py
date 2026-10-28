"""T7 — 5.1.1 – 17: the cha group (prāk krītāc chaḥ, 5.1.1). tasmai hitam / tadarthaṃ vikṛteḥ prakṛtau / tadasya tadasmin syāt open a frame;
cha (5.1.1) attaches to every stem; the specials (yat, thyan, kha, ṇa, ḍhañ, khañ, ñya, añ) are apavādas."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

CASES = [   # (stem, lexical tags, sense, extra vivakṣā, form that must be one of the readings)
    ("vatsa", None, "tasmEhita", {}, "vatsIyaH"),                      # 5.1.5 + 5.1.1
    ("go", None, "tasmEhita", {}, "gavyaH"),                           # 5.1.2 gavādi
    ("zaNku", None, "tasmEhita", {}, "zaNkavyaH"),                     # uvarṇānta
    ("kambala", None, "tasmEhita", {"arthaViSeSa": "saMjYA"}, "kambalyaH"),    # 5.1.3
    ("apUpa", None, "tasmEhita", {}, "apUpyaH"),                       # 5.1.4 vā
    ("apUpa", None, "tasmEhita", {}, "apUpIyaH"),
    ("danta", {"lex:SarIrAvayava"}, "tasmEhita", {}, "dantyaH"),       # 5.1.6
    ("Kala", None, "tasmEhita", {}, "KalyaH"),                         # 5.1.7
    ("aja", None, "tasmEhita", {}, "ajaTyaH"),                         # 5.1.8
    ("Atman", None, "tasmEhita", {}, "AtmanInaH"),                     # 5.1.9
    ("sarva", None, "tasmEhita", {}, "sArvaH"),                        # 5.1.10
    ("puruza", None, "tasmEhita", {}, "pOruzeyaH"),
    ("mARava", None, "tasmEhita", {}, "mARavInaH"),                    # 5.1.11
    ("fzaBa", None, "prakfti", {}, "ArzaByaH"),                        # 5.1.14
    ("vardhra", None, "prakfti", {}, "vArdhraH"),                       # 5.1.15
    ("pariKA", None, "syAt", {}, "pAriKeyaH"),                         # 5.1.17
    ("kumBa", None, "syAt", {}, "kumBIyaH"),                           # 5.1.16 + 5.1.1
]


@pytest.mark.xfail(strict=True, reason="S15: ṣatva of the prātipadika's s (chadis → chādiṣeya) is not modelled")
def test_chadis_satva():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("Cadis", 1, 1, "pulliṅga", taddhitArtha="prakfti"))}
    assert "CAdizeyaH" in got, sorted(got)


@pytest.mark.parametrize("stem,og,sense,extra,want", CASES, ids=lambda c: None)
def test_sense(stem, og, sense, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "pulliṅga", origin_tags=og, taddhitArtha=sense, **extra))}
    assert want in got, sorted(got)
