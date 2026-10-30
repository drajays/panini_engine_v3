"""AMENDMENT 27 — the svārthika sūtras (5.4.7, 8, 13 – 15, 23, 27 – 29, 34, 38, 39): `taddhitArtha=svArTa`, no sense frame, the vā reading stands aside."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.taddhita_loop import derive_taddhita, derive_taddhita_stem

N, P, S = "napuṃsaka", "pulliṅga", "strīliṅga"
DIK = {"lex:dikSabda"}
CASES = [   # (stem, origin tags, linga, a form that must be among the readings, the plain reading the vā keeps or None)
    ("azaqakza", None, N, "azaqakzIRam", "azaqakzam"),            # 5.4.7
    ("alaMkarman", None, N, "alaNkarmIRam", None),
    ("alampuruza", None, N, "alampuruzIRam", "alampuruzam"),
    ("ASitaNgu", None, N, "ASitaNgavInam", "ASitaNgu"),
    ("prAc", None, N, "prAcInam", "prAk"),                         # 5.4.8
    ("arvAc", None, N, "arvAcInam", "arvAk"),
    ("anugAdin", None, P, "AnugAdikaH", None),                     # 5.4.13
    ("ananta", None, N, "Anantyam", "anantam"),                    # 5.4.23
    ("AvasaTa", None, N, "AvasaTyam", "AvasaTam"),
    ("itiha", None, N, "Etihyam", "itiham"),
    ("Bezaja", None, N, "BEzajyam", "Bezajam"),
    ("deva", None, S, "devatA", None),                             # 5.4.27
    ("avi", None, P, "avikaH", None),                              # 5.4.28
    ("yAva", None, P, "yAvakaH", None),                            # 5.4.29
    ("maRi", None, P, "maRikaH", None),
    ("vinaya", None, N, "vEnayikam", "vinayam"),                   # 5.4.34
    ("samaya", None, N, "sAmayikam", "samayam"),
    ("prajYa", None, N, "prAjYam", None),                          # 5.4.38
    ("mfd", None, S, "mfttikA", "mft"),                            # 5.4.39
    ("saMrAvin", {"origin_pratyaya:inuR"}, N, "sAMrAviRam", None),  # 5.4.15
]


def _forms(stem, og, linga, **vivaksha):
    return {b.surface_slp1 for b in explore(lambda: derive_taddhita(stem, 1, 1, linga, origin_tags=og, **vivaksha))}


@pytest.mark.parametrize("stem,og,linga,want,plain", CASES, ids=lambda c: None)
def test_svarthika_reading(stem, og, linga, want, plain):
    got = _forms(stem, og, linga, taddhitArtha="svArTa")
    assert want in got, sorted(got)
    if plain:
        assert plain in got, sorted(got)      # the vā: the word without the pratyaya stays


@pytest.mark.parametrize("stem,og,linga,nowant", [("avi", None, P, "avikaH"), ("deva", None, S, "devatA"), ("yAva", None, P, "yAvakaH"), ("ananta", None, N, "Anantyam")], ids=lambda c: None)
def test_no_svarthika_without_the_value(stem, og, linga, nowant):
    got = _forms(stem, og, linga, taddhitArtha="apatya")
    assert nowant not in got, sorted(got)


@pytest.mark.parametrize("stem,og,linga", [("aSva", None, N), ("prAc", DIK, N)], ids=lambda c: None)
def test_stem_outside_the_condition_gets_nothing(stem, og, linga):
    got = _forms(stem, og, linga, taddhitArtha="svArTa")
    assert not any(w.startswith(("aSvIn", "aSvik", "prAcIn")) for w in got), sorted(got)


def test_nac_anta_aN():
    stem, tags, multi = derive_taddhita_stem("vyAvakroSI", {"origin_pratyaya:Rac"}, None, taddhitArtha="svArTa")
    assert stem == "vyAvakroSa" and "origin_pratyaya:aY" in tags and "5.4.14" in multi      # 5.4.14 añ after a ṇac-anta; ṅīp restores the ī in the feminine
