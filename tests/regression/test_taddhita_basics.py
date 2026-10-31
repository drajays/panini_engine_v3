"""Taddhita-prakriyā basics (owner's teaching deck: pañca-mahotsarga, it-saṃjñā 1.3.2-9 and what each it-letter is for, aṅga/bha/pada
1.4.13-19, ṭi-lopa, vṛddhi 7.2.117-118, svara 6.1.x, strī-pratyaya 4.1.15/41). Passing cases pin what the loop already does by rule;
strict xfails are gaps / wrong order, with the reason. See docs/TADDHITA_BASICS_CHECK.md. No engine change.

Stems are compared before the sup (the derived stem is a prātipadika, 1.2.46); ``steps`` is the loop's own application order."""
from functools import lru_cache

import pytest

import sutras  # noqa: F401
from engine.tape_init.taddhita import build_taddhita_state
from engine.vikalpa import explore
from tools.autonomy_report import run_autonomously

SAMKHYA = frozenset({"lex:saMKyA"})


def _run(stem, og, **viv):
    s = build_taddhita_state(stem, set(og) if og else None, **viv)
    s.phase = "upadesha"
    run = run_autonomously(s, "", stem, 300, stop_before_tripadi=True)
    run.state.meta["_steps"] = [x[0] for x in run.steps]
    return run.state


@lru_cache(maxsize=None)
def derive(stem, artha, og=frozenset()):
    """{stem surface: application order of the sūtras} over every vikalpa reading."""
    out = {}
    for b in explore(lambda: _run(stem, og, taddhitArtha=artha)):
        out.setdefault(b.surface_slp1, b.state.meta["_steps"])
    return out


# --- the five mahotsargas: the default pratyaya of the domain, chosen by the sense (artha) alone -----------------------------------
DOMAINS = [   # (stem, artha, lexical tags, stem that must be a reading)
    ("upagu", "apatya", frozenset(), "Opagava"),            # 4.1.83 aṇ
    ("akza", "dIvyati", frozenset(), "Akzika"),             # 4.4.1 ṭhak
    ("go", "tasmEhita", frozenset(), "gavya"),              # 4.4.75 yat group
    ("vatsa", "tasmEhita", frozenset(), "vatsIya"),         # 5.1.1 cha
    ("godAna", "krIta", frozenset(), "gOdAnika"),           # 5.1.18 ṭhañ
]


@pytest.mark.parametrize("stem,artha,og,want", DOMAINS, ids=[d[3] for d in DOMAINS])
def test_mahotsarga_by_sense(stem, artha, og, want):
    assert want in derive(stem, artha, og), sorted(derive(stem, artha, og))


# --- it-lopa, aṅga, vṛddhi, ṭi-lopa: forms and order -------------------------------------------------------------------------------
FORMS = [
    ("aSvapati", "apatya", frozenset(), "ASvapata"),         # ṇit: ādivṛddhi 7.2.117
    ("dakza", "apatya", frozenset(), "dAkzi"),              # ñit iñ: vṛddhi
    ("pfTivI", "apatya", frozenset(), "pArTiva"),           # ñit añ
    ("dadhi", "tenasaMskfta", frozenset(), "dAdhika"),      # kit ṭhak: vṛddhi 7.2.118
    ("triMSat", "tasyapUraRa", SAMKHYA, "triMSa"),          # ḍit ḍaṭ: ṭi-lopa 6.4.143
    ("ekAdaSan", "tasyapUraRa", frozenset({"lex:saMKyA", "lex:saMKyAdi"}), "ekAdaSa"),    # ḍit: ṭi-lopa
    ("naqa", "asti", frozenset(), "naqvala"),               # ḍit ḍvalac
    ("jana", "samUha", frozenset(), "janata"),              # tal: l is it (1.3.3)
]


@pytest.mark.parametrize("stem,artha,og,want", FORMS, ids=[f[3] for f in FORMS])
def test_forms(stem, artha, og, want):
    assert want in derive(stem, artha, og), sorted(derive(stem, artha, og))


def _steps(stem, artha, want, og=frozenset()):
    return derive(stem, artha, og)[want]


def test_itlopa_then_prAtipadika_then_anga():
    s = _steps("dakza", "apatya", "dAkzi")
    assert s.index("1.3.3") < s.index("1.3.9") < s.index("1.2.46") < s.index("1.4.13")      # it-saṃjñā, lopa, prātipadika, aṅga


def test_itletter_1_3_7_cutu_for_dit():
    s = _steps("triMSat", "tasyapUraRa", "triMSa", SAMKHYA)
    assert "1.3.7" in s and s.index("1.3.7") < s.index("1.3.9") < s.index("6.4.143")


def test_bha_before_vrddhi_nit_ait():
    s = _steps("dakza", "apatya", "dAkzi")
    assert s.index("1.4.18") < s.index("7.2.117")                       # bha 1.4.18 before ñit vṛddhi


def test_kit_vrddhi_before_ti_lopa():
    s = _steps("dadhi", "tenasaMskfta", "dAdhika")
    assert s.index("7.2.118") < s.index("6.4.148")


def test_pada_1_4_17_before_consonant_initial_taddhita():
    assert "1.4.17" in _steps("jana", "samUha", "janata")


# --- gaps / wrong order -------------------------------------------------------------------------------------------------------------------
def test_ti_lopa_after_vrddhi_for_nit_ait():       # 7.2.117 is later than 6.4.148: paratva, and the teaching, put vṛddhi first
    s = _steps("dakza", "apatya", "dAkzi")
    assert s.index("7.2.117") < s.index("6.4.148")


test_ti_lopa_after_vrddhi_for_nit_ait = pytest.mark.xfail(strict=True, reason="wrong-order: loop applies 6.4.148 before 7.2.117 (same surface); teaching: vṛddhi then yasyeti ca")(
    test_ti_lopa_after_vrddhi_for_nit_ait)


@pytest.mark.xfail(strict=True, reason="wrong-order: 1.4.17 pada is decided before the ṭhasyekaḥ ādeśa 7.3.50; the teaching decides ajādi/halādi after ādeśa")
def test_pada_bha_decided_after_adesha():
    s = _steps("dadhi", "tenasaMskfta", "dAdhika")
    assert s.index("7.3.50") < s.index("1.4.17")


@pytest.mark.xfail(strict=True, reason="gap: no svara sūtra (6.1.164/165/185/197/217, 3.1.4) fires in the taddhita loop; accent is not modelled on the stem")
@pytest.mark.parametrize("stem,artha,want,sid", [("dadhi", "tenasaMskfta", "dAdhika", "6.1.165"), ("aSvapati", "apatya", "ASvapata", "6.1.197")])
def test_svara_by_itletter(stem, artha, want, sid):
    assert sid in _steps(stem, artha, want)


GAPS = [   # (stem, artha, lex tags, form the teaching gives, reason)
    ("garut", "asti", frozenset(), "garutmat", "matup 5.2.94 is armed only by a recipe (matup_recipe), not chosen by the loop: engine gives gAruta (aṇ)"),
    ("kumuda", "asti", frozenset(), "kumudvat", "same: matup / vatup (1.3.2 u~) never reached in the loop; engine gives kOmuda"),
    ("yaSas", "asti", frozenset(), "yaSasvin", "vini 5.2.121 not reached; engine gives yASasa"),
    ("vinatA", "apatya", frozenset(), "vEnateya", "ḍhak 4.1.119-20 (kit, gives -eya) not reached; engine gives vEnata"),
    ("Barata", "apatya", frozenset(), "BArateya", "ḍhak not reached; engine gives BArata"),
    ("SuBra", "apatya", frozenset(), "SOBreya", "4.1.123 ḍhak not reached"),
    ("mfkaRqu", "apatya", frozenset(), "mArkaRqeya", "ḍhak not reached; engine gives mArkaRqava"),
    ("goDA", "apatya", frozenset(), "gODeya", "ḍhak not reached; engine gives gODa"),
    ("parSu", "apatya", frozenset(), "pArSva", "ṇas 4.1.? (sit, pada) not reached; engine gives pArSava"),
    ("kraya", "krIta", frozenset(), "kraya" + "ika", "the deck's ṇit/nit illustration kraya+ṭhan -> krayika (no vṛddhi): loop picks ṭhak and gives krAyika"),
]


@pytest.mark.xfail(strict=True, reason="gap: see GAPS")
@pytest.mark.parametrize("stem,artha,og,want,why", GAPS, ids=[g[3] for g in GAPS])
def test_gap(stem, artha, og, want, why):
    assert want in derive(stem, artha, og), why
