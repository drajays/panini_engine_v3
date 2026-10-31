"""Taddhita-prakriyā deck 2 (owner's teaching deck on pratyaya-ādeśa: it-lopa, then 7.1.2 [kha gha cha ṭha ḍha pha -> īn iya īya ik eya āyan],
7.1.1 [yu vu -> ana aka], 7.3.50 ṭhasyekaḥ, 7.3.51 isusuktāntāt kaḥ, 6.1.67 apṛkta vi-lopa, then aṅga/sandhi).
Passing cases pin what the loop already does by rule; strict xfails are gaps / wrong order, with the reason. See docs/TADDHITA_2_CHECK.md.
Engine untouched. Surfaces are the loop's stem before the tripāḍī (m->n 8.4.58, s->z 8.3.59 come later)."""
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
def derive(stem, artha, og=frozenset(), extra=()):
    """{stem surface: application order of the sūtras} over every vikalpa reading (``extra``: more vivakṣā pairs)."""
    out = {}
    for b in explore(lambda: _run(stem, og, taddhitArtha=artha, **dict(extra))):
        out.setdefault(b.surface_slp1, b.state.meta["_steps"])
    return out


# --- 7.1.2 / 7.1.1: the first letter of the pratyaya is replaced (deck slides "pratyayādeśaḥ 1-8") ---------------------------------
ADESA = [   # (stem, artha, form, sūtra that must be in the trace)
    ("yuzmad", "idam", "yOzmAkIna", "7.1.2"),        # kha -> īn (4.3.1 KaY)
    ("prAc", "svArTa", "prAcIna", "7.1.2"),          # kha -> īn (5.4.8)
    ("rAzwra", "Bava", "rAzwriya", "7.1.2"),         # gha -> iya (4.2.93)
    ("ASAQa", "Bava", "ASAQIya", "7.1.2"),           # cha -> īya
    ("kASI", "Bava", "kASIya", "7.1.2"),             # cha -> īya (the engine picks cha here; see the 4.2.116 xfail)
    ("kuYja", "apatya", "kOYjAyana", "7.1.2"),       # pha -> āyana (cPaY)
    ("sAyam", "kAle", "sAyamtana", "7.1.1"),         # yu -> ana, tuṭ (4.3.23 tyul)
    ("ciram", "kAle", "ciramtana", "7.1.1"),         # yu -> ana, tuṭ (4.3.23 tyu)
    ("viMSati", "krIta", "viMSaka", "7.1.1"),        # vu -> aka (5.1.24 qvun), ti-lopa 6.4.142
]


@pytest.mark.parametrize("stem,artha,want,sutra", ADESA, ids=[a[2] for a in ADESA])
def test_adesa(stem, artha, want, sutra):
    og = SAMKHYA if stem == "viMSati" else frozenset()
    d = derive(stem, artha, og)
    assert want in d, sorted(d)
    assert sutra in d[want]


def test_iha_ha_pratyaya():
    assert "iha" in derive("idam", "saptamIvib")           # idam + ha -> iha (5.3.11); 1.1.38 avyaya follows


def test_itlopa_before_adesa_before_anga():
    s = derive("kuYja", "apatya")["kOYjAyana"]
    assert s.index("1.3.9") < s.index("7.1.2") < s.index("1.4.18")      # deck: it-lopa, then pratyayādeśa, then aṅgakārya


def test_adesa_before_bha_for_gha():
    s = derive("rAzwra", "Bava")["rAzwriya"]
    assert s.index("7.1.2") < s.index("1.4.18") < s.index("6.4.148")


def test_thak_ik_7_3_50():
    s = derive("akza", "dIvyati")["Akzika"]
    assert "7.3.50" in s


# --- 7.3.51 and the order of 7.3.50 / 7.3.51 / 7.2.118 (ORDER_BEFORE in engine/resolver.py) ---------------------------------------------
@pytest.mark.parametrize("stem,want", [("sarpis", "sArpiska"), ("Danus", "DAnuska"), ("Denu", "DEnuka"), ("yakft", "yAkftka")])
def test_7_3_51_tha_to_ka(stem, want):
    assert want in derive(stem, "tenasaMskfta", SAMKHYA if stem == "yakft" else frozenset())      # is / us / uk / t-final aṅga: ṭh -> k, apavāda of 7.3.50


@pytest.mark.xfail(strict=True, reason="vārttika 'doṣa upasaṅkhyānam' (Kāśikā 7.3.51: dauṣkaḥ): no sūtra row carries it, and doṣ (…oṣ) is not is / us / uk / t-final; Art. 18 gap, not code")
def test_7_3_51_dos_varttika():
    assert "dOzka" in derive("doz", "tenasaMskfta")


def test_7_3_50_before_7_2_118():
    s = derive("akza", "dIvyati")["Akzika"]
    assert s.index("7.3.50") < s.index("7.2.118")      # ṭh -> ik is the pratyaya's own ādeśa: it precedes the aṅga's kiti ca vṛddhi


def test_7_3_51_instead_of_7_3_50():
    s = derive("sarpis", "tenasaMskfta")["sArpiska"]
    assert "7.3.51" in s and "7.3.50" not in s and s.index("7.3.51") < s.index("7.2.118")


# --- gaps -----------------------------------------------------------------------------------------------------------------------
def test_bhavadiya_4_2_115():
    d = derive("Bavat", "Bava")      # bhavat (the word the sūtra names); chas -> īya, ṭhak -> ka (7.3.51, t-final); d for t is 8.2.39, after this stage
    assert {"BavatIya", "BAvatka"} <= set(d), sorted(d)


def test_kasika_4_2_116():
    assert "kASika" in derive("kASi", "Bava")      # kāśi (Gaṇapāṭha, short i) + ṭhañ; ñiṭh gives the same stem (strī / svara differ)


def test_glucukayani_phin():
    d = derive("glucuka", "apatya", extra=(("arthaViSeSa", "prAcAm"),))      # 4.1.160 prācām avṛddhāt phiñ bahulam (the sūtra the Kāśikā gives; 4.1.90 is yūni luk)
    assert "glucukAyani" in d and "glOcuki" in d, sorted(d)      # bahulam: the iñ reading stays


@pytest.mark.xfail(strict=True, reason="cvi (5.4.50 abhūtatadbhāve kṛbhvastiyoge sampadyakartari cviḥ) + apṛkta-vi 6.1.67 beyond the kvip flag: the sense abhūtatadbhāva is not in the closed vivakṣā vocabulary and no Art. 22 owner ruling (brain rulings/R-*) admits it; 6.1.67 stays the kvip-residue flag. Not added without a ruling")
def test_cvi_sukli():
    assert "SuklI" in derive("Sukla", "abhUtatadBAva")
