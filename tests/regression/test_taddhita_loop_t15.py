"""T15 — iṣṭhan / īyasun after a guṇavacana (5.3.55, 5.3.57; the niyama 5.3.58 is the caller's `lex:guRavacana`) and what happens to the aṅga before them:
6.4.154 – 160 (tṛ-lopa, ṭi-lopa, yaṇādi-lopa + guṇa, the ādeśas, bahu → bhū, yiṭ, jyād ādīyasaḥ) and the stem ādeśas 5.3.61 – 64.
Forms are those of the Kāśikā on 6.4.154 – 159 and 5.3.61 – 65."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita

G = {"lex:guRavacana"}
DV = {"arthaViSeSa": "dvivacanavibhajya"}
CASES = [   # (stem, extra vivakṣā, a form that must be among the readings)
    ("paWu", {}, "paWizWam"),                 # 6.4.155
    ("paWu", DV, "paWIyaH"),
    ("laGu", {}, "laGizWam"),
    ("laGu", DV, "laGIyaH"),
    ("kartf", {}, "karizWam"),                # 6.4.154
    ("kartf", DV, "karIyaH"),
    ("sTUla", {}, "sTavizWam"),               # 6.4.156
    ("sTUla", DV, "sTavIyaH"),
    ("dUra", {}, "davizWam"),
    ("dUra", DV, "davIyaH"),
    ("yuvan", {}, "yavizWam"),
    ("yuvan", DV, "yavIyaH"),
    ("hrasva", {}, "hrasizWam"),
    ("kzipra", {}, "kzepizWam"),
    ("kzipra", DV, "kzepIyaH"),
    ("kzudra", {}, "kzodizWam"),
    ("kzudra", DV, "kzodIyaH"),
    ("uru", {}, "varizWam"),                  # 6.4.157
    ("uru", DV, "varIyaH"),
    ("bahula", {}, "baMhizWam"),
    ("guru", {}, "garizWam"),
    ("guru", DV, "garIyaH"),
    ("vfdDa", {}, "varzizWam"),               # 6.4.157, the other reading of 5.3.62
    ("vfdDa", DV, "varzIyaH"),
    ("tfpra", {}, "trapizWam"),
    ("dIrGa", {}, "drAGizWam"),
    ("vfndAraka", {}, "vfndizWam"),
    ("bahu", {}, "BUyizWam"),                 # 6.4.159
    ("antika", {}, "nedizWam"),               # 5.3.63
    ("antika", DV, "nedIyaH"),
    ("bAQa", {}, "sADizWam"),
    ("bAQa", DV, "sADIyaH"),
    ("yuvan", {}, "kanizWam"),                # 5.3.64
    ("yuvan", DV, "kanIyaH"),
    ("alpa", {}, "kanizWam"),
    ("alpa", {}, "alpizWam"),                 # the vā: 6.4.155
    ("alpa", DV, "kanIyaH"),
]
XFAIL = [   # the pratyaya / ādeśa is the sūtra's own; the form waits for the engine fix in the reason
    ("priya", {}, "prezWam", "it_lopa_already_done: after 6.1.87 fuses the stem's a with the i of iSWa the pratyaya Term is re-examined and its z is taken as ādi (1.3.6)"),
    ("sTira", {}, "sTezWam", "same: 6.1.87 across the stem / pratyaya boundary, then 1.3.6 on the new ādi z"),
    ("praSasya", {}, "jyezWam", "same (5.3.61 jya + iSWa)"),
    ("vfdDa", {}, "jyezWam", "same (5.3.62)"),
    ("praSasya", DV, "jyAyaH", "same: jya + Ayas fuse by 6.1.101, then 1.3.3 takes the final s as it"),
    ("bahu", DV, "BUyaH", "6.4.146 (its ū extension for taddhita) turns bhū + yas into bhavya; the extension needs an audit"),
]


@pytest.mark.parametrize("stem,extra,want", CASES, ids=lambda c: None)
def test_forms(stem, extra, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=G, taddhitArtha="atiSAyana", **extra))}
    assert want in got, sorted(got)


@pytest.mark.parametrize("stem,extra,want,why", XFAIL, ids=lambda c: None)
@pytest.mark.xfail(strict=True, reason="known gap")
def test_known_gaps(stem, extra, want, why):
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, "napuṃsaka", origin_tags=G, taddhitArtha="atiSAyana", **extra))}
    assert want in got, why


def test_iSWan_only_after_guRavacana():
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("pAcaka", 1, 1, "napuṃsaka", taddhitArtha="atiSAyana"))}
    assert "pAcakatamam" in got and not any("izWa" in x for x in got), sorted(got)      # 5.3.58: pācakatama, not pācakiṣṭha
