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
def derive(stem, artha, og=frozenset()):
    """{stem surface: application order of the sūtras} over every vikalpa reading."""
    out = {}
    for b in explore(lambda: _run(stem, og, taddhitArtha=artha)):
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


# --- gaps -----------------------------------------------------------------------------------------------------------------------
@pytest.mark.xfail(strict=True, reason="7.3.51 isusuktāntāt kaḥ is inert (act only sets a meta flag, no ṭh -> k): ṭhak after is/us/u/ṛ/t-final aṅga and doṣ "
                   "gives ik (sArpisika, DAnusika, DEnavika, yAkftika, dOzika) instead of ka; the apavāda of 7.3.50 never applies")
@pytest.mark.parametrize("stem,want", [("sarpis", "sArpiska"), ("Danus", "DAnuska"), ("Denu", "DEnuka"), ("yakft", "yAkftka"), ("doz", "dOzka")])
def test_7_3_51_tha_to_ka(stem, want):
    assert want in derive(stem, "tenasaMskfta", SAMKHYA if stem == "yakft" else frozenset())


@pytest.mark.xfail(strict=True, reason="wrong order: deck (Kāśikā 7.3.50 revatī + ṭhak) does 7.3.50 ṭh -> ik first, then 7.2.118 kiti ca vṛddhi; the loop does 7.2.118 first")
def test_7_3_50_before_7_2_118():
    s = derive("akza", "dIvyati")["Akzika"]
    assert s.index("7.3.50") < s.index("7.2.118")


@pytest.mark.xfail(strict=True, reason="4.2.115 bhavataṣṭhak-chasau is not loop-driven: bhavatī + sense bhava gives BAvata (aṇ), not BavadIya")
def test_bhavadiya_4_2_115():
    assert "BavadIya" in derive("BavatI", "Bava")


@pytest.mark.xfail(strict=True, reason="4.2.116 kāśyādibhyaṣṭhañiṭhau is not loop-driven: kāśī gives kASIya (cha), not kASika (ṭhañ, ṭh -> ik)")
def test_kasika_4_2_116():
    assert "kASika" in derive("kASI", "Bava")


@pytest.mark.xfail(strict=True, reason="4.1.90 phiñ (glucukādi, ph -> āyan) is not loop-driven: glucuka + apatya gives glOcuki (iñ), not glucukAyani")
def test_glucukayani_phin():
    assert "glucukAyani" in derive("glucuka", "apatya")
