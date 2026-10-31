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
    ("SuBra", "apatya", frozenset(), "SOBreya"),            # 4.1.123 ḍhak (śubhrādi): ḍ it, 7.1.2 Q -> eya, kit vṛddhi 7.2.118, 6.4.148
    ("Barata", "apatya", frozenset(), "BArateya"),          # śubhrādi, over utsādi añ 4.1.86
    ("goDA", "apatya", frozenset(), "gODeya"),              # śubhrādi (Kāśikā 4.1.129: gaudheyo 'pi)
    ("garut", "astyasya", frozenset(), "garutmat"),         # 5.2.94 matup (vivakṣā astyasya): u~ it (1.3.2), p it (1.3.3)
    ("yaSas", "astyasya", frozenset(), "yaSasvin"),         # 5.2.121 vini (a stem in as): ṅi's final i... vini: n stays, 1.4.19 pada-sañjñā aside
]


@pytest.mark.parametrize("stem,artha,og,want", FORMS, ids=[f[3] for f in FORMS])
def test_forms(stem, artha, og, want):
    assert want in derive(stem, artha, og), sorted(derive(stem, artha, og))


def test_kumudvat_by_dmatup_and_jhayah():
    """kumuda + 4.2.87 ḍmatup (cāturarthika, 'asti'): ḍ it (1.3.7), ṭi-lopa 6.4.143, m -> v by 8.2.10 jhayaḥ."""
    from pipelines.taddhita_loop import derive_taddhita
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("kumuda", 1, 1, "puMliNga", taddhitArtha="asti"))}
    assert "kumudvAn" in got, sorted(got)


@pytest.mark.xfail(strict=True, reason="gap (S45/S52): naqa has 4.2.87 ḍmatup (naqvAn) and 4.2.88 ḍvalac (naqvalaH); the loop does not explore between two competing sūtras, para 4.2.88 wins")
def test_naqvan_both_readings():
    from pipelines.taddhita_loop import derive_taddhita
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("naqa", 1, 1, "puMliNga", taddhitArtha="asti"))}
    assert {"naqvAn", "naqvalaH"} <= got, sorted(got)


def test_matup_vini_by_rule():
    assert {"1.3.2", "1.3.3", "1.3.9"} <= set(_steps("garut", "astyasya", "garutmat"))      # matu~p: u~ (1.3.2), p (1.3.3), lopa
    assert "1.4.19" in _steps("yaSas", "astyasya", "yaSasvin")                           # tasau matvarthe: bha, so yaśas is not pada
    from pipelines.taddhita_loop import derive_taddhita
    got = {b.surface_slp1 for b in explore(lambda: derive_taddhita("garut", 1, 2, "puMliNga", taddhitArtha="astyasya"))}
    assert "garutmantO" in got, sorted(got)                                               # 7.2.70 ugit num (u~ of matup)


def test_dhak_after_strI_chain():
    """vinatā: strī stem (4.1.4 ṭāp, recorded as its last pratyaya) + 4.1.120 strībhyo ḍhak -> vainateya, not aṇ."""
    from pipelines import chain
    st = chain.taddhita(chain.strI(chain.Stem("vinata")), taddhitArtha="apatya")
    assert st.slp1 == "vEnateya" and "4.1.120" in st.trace[-1][1], (st.slp1, st.trace[-1][1][:12])


@pytest.mark.parametrize("stem,artha,want", [("upagu", "apatya", "OpagavI"), ("akza", "dIvyati", "AkzikI"), ("dadhi", "tenasaMskfta", "dAdhikI")])
def test_strI_after_taddhita_nip_4_1_15(stem, artha, want):
    """aṇ / ṭhak (listed in 4.1.15; ika is ṭhak by sthānivat) + striyām: ṅīp, not ṭāp (4.1.15 apavāda of 4.1.4); a lopa 6.4.148 (bha, 1.4.18 for the strī-pratyaya)."""
    from pipelines import chain
    st = chain.strI(chain.taddhita(chain.Stem(stem), taddhitArtha=artha))
    ids = {i for _, x in st.trace[-1:] for i in x}
    assert st.slp1 == want and "4.1.15" in ids and "4.1.4" not in ids, (st.slp1, sorted(ids))


@pytest.mark.parametrize("stem,tags,want", [("gOra", (), "gOrI"), ("Sudra", ("origin_it:z",), "SudrI")], ids=["gaurAdi", "zit"])
def test_strI_nis_4_1_41(stem, tags, want):
    """ṅīṣ: a gaurādi word (gaura) or a stem made by a ṣit pratyaya (the origin record carries its it-letter ṣ)."""
    from pipelines import chain
    st = chain.strI(chain.Stem(stem, frozenset(tags)))
    assert st.slp1 == want and "4.1.41" in {i for _, x in st.trace[-1:] for i in x}, st.slp1


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


# --- order (Art. 21: declared ordering in CONFLICT_OVERRIDES / 1.4.17 waits for the pratyaya's ādeśa) -------------------------------------
def test_vrddhi_before_ti_lopa_for_nit_ait():       # 7.2.117 (para) before yasyeti ca 6.4.148
    s = _steps("dakza", "apatya", "dAkzi")
    assert s.index("7.2.117") < s.index("6.4.148")


def test_pada_bha_decided_after_adesha():
    s = _steps("dadhi", "tenasaMskfta", "dAdhika")
    assert s.index("7.3.50") < s.index("1.4.18") and "1.4.17" not in s    # ika is yac-initial: bha, never pada


# --- gaps ---------------------------------------------------------------------------------------------------------------------------------
@pytest.mark.xfail(strict=True, reason="blocked (Amendment 25): samarthatā (2.1.1 / 4.1.82 samarthānāṃ prathamāt: vyapekṣā or ekārthībhāva between the base and the word it is related to) needs the related word on the tape and a vivakṣā value that some sūtra's samagra names; neither exists (data/inputs/vivaksha_schema.json has no such key, and the schema is built from the samagras, not typed). The sense value taddhitArtha alone licenses the pratyaya")
def test_samarthata_is_a_named_gate():
    from engine.vivaksha import schema
    assert "samarTatA" in schema()      # a closed, cited vivakṣā key for the sāmarthya the speaker intends


@pytest.mark.xfail(strict=True, reason="gap: no svara sūtra (6.1.164/165/185/197/217, 3.1.4) fires in the taddhita loop; accent is not modelled on the stem")
@pytest.mark.parametrize("stem,artha,want,sid", [("dadhi", "tenasaMskfta", "dAdhika", "6.1.165"), ("aSvapati", "apatya", "ASvapata", "6.1.197")])
def test_svara_by_itletter(stem, artha, want, sid):
    assert sid in _steps(stem, artha, want)


GAPS = [   # (stem, artha, lex tags, form the teaching gives, reason)
    ("mfkaRqu", "apatya", frozenset(), "mArkaRqeya", "Art. 22 data conflict: Kāśikā 4.1.123 lists मृकण्डु (mfkaRqu) but data/inputs/ganapatha_full.json has sfkaRqu in SuBrAdiH, so the gaṇa test fails; needs an owner ruling / upstream correction, not a code change"),
    ("kraya", "krIta", frozenset(), "kraya" + "ika", "the deck's ṇit/nit illustration kraya+ṭhan -> krayika (no vṛddhi): loop picks ṭhak and gives krAyika"),
]


def test_parsu_nas_vartika():
    """Bhāṣya 4.2.43 vā. 4 पर्श्वा णस् वक्तव्यः, living in 4.2.43 (Art. 25): parśu + ṇas = pārśva, pada by 1.4.16 (sit) so no guṇa."""
    assert "pArSva" in derive("parSu", "samUha")


@pytest.mark.xfail(strict=True, reason="gap: see GAPS")
@pytest.mark.parametrize("stem,artha,og,want,why", GAPS, ids=[g[3] for g in GAPS])
def test_gap(stem, artha, og, want, why):
    assert want in derive(stem, artha, og), why
