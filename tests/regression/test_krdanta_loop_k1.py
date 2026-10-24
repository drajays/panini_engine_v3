"""K1 — the first kṛt families through the recipe-free loop, from a *meaning* (AMENDMENT 25, addendum 2026-10-24), never from a named affix:
niṣṭhā 3.2.102 (kta in karmaṇi / bhāve, ktavatu for the kartṛ — 3.4.70, 3.4.67), the kṛtyas 3.1.95–96 (तव्यत् तव्य अनीयर्: the sūtra lists three, the
reading takes one — engine.vikalpa), ṇvul-tṛcau 3.1.133 and tumun-ṇvulau 3.3.10 (भविष्यति, क्रियार्थायाम्). Forms are Kāśikā udāharaṇas
(3.1.96 कर्तव्यम्, करणीयम्; 3.1.133 कारकः, कर्ता; 3.2.102 कृतम्, कृतवान्; 3.3.10 कर्तुम्)."""
import pytest

import sutras  # noqa: F401
from engine.vikalpa import explore
from pipelines.krdanta import derive_krdanta, derive_krdanta_stem

KTA = dict(kala="BUta", artha="karman")
KTAVATU = dict(kala="BUta", artha="kartf")
KRTYA = dict(krt="kftya")
AGENT = dict(krt="Rvultfc")

CASES = [   # (dhātu, vibhakti, vacana, liṅga, vivakṣā, form that must be one of the readings)
    ("qukfY", 1, 1, "pulliṅga", KTA, "kftaH"),              # कृतः
    ("qukfY", 1, 1, "pulliṅga", KTAVATU, "kftavAn"),        # कृतवान्
    ("BvAdi_01_0001", 1, 1, "pulliṅga", KTA, "BUtaH"),
    ("BvAdi_01_1137", 1, 1, "pulliṅga", KTA, "gataH"),      # गतः
    ("BvAdi_01_1137", 1, 1, "pulliṅga", KTAVATU, "gatavAn"),
    ("RIY", 1, 1, "pulliṅga", KTA, "nItaH"),
    ("RIY", 1, 1, "pulliṅga", KTAVATU, "nItavAn"),
    ("BvAdi_01_0381", 1, 1, "pulliṅga", KTA, "paWitaH"),    # पठितः
    ("BvAdi_01_1092", 1, 1, "pulliṅga", KTA, "SrutaH"),
    ("qukfY", 1, 2, "napuṃsaka", KRTYA, "kartavye"),        # कर्तव्ये
    ("qukfY", 1, 1, "napuṃsaka", KRTYA, "karaRIyam"),       # करणीयम्
    ("qukfY", 1, 1, "napuṃsaka", KRTYA, "kartavyam"),       # कर्तव्यम्
    ("BvAdi_01_1137", 1, 1, "napuṃsaka", KRTYA, "gantavyam"),
    ("RIY", 1, 1, "napuṃsaka", KRTYA, "netavyam"),
    ("BvAdi_01_1092", 1, 1, "napuṃsaka", KRTYA, "Srotavyam"),
    ("qukfY", 1, 1, "pulliṅga", AGENT, "kArakaH"),          # कारकः
    ("qukfY", 1, 1, "pulliṅga", AGENT, "kartA"),            # कर्ता
    ("RIY", 1, 1, "pulliṅga", AGENT, "nAyakaH"),
    ("RIY", 1, 1, "pulliṅga", AGENT, "netA"),
    ("qupaca~z", 1, 1, "pulliṅga", AGENT, "pAcakaH"),
    ("qupaca~z", 1, 1, "pulliṅga", AGENT, "paktA"),
]


@pytest.mark.parametrize("ref,vib,vac,linga,viv,want", CASES, ids=[f"{c[0]}-{c[5]}" for c in CASES])
def test_krdanta_from_meaning(ref, vib, vac, linga, viv, want):
    got = {b.surface_slp1 for b in explore(lambda: derive_krdanta(ref, vib, vac, linga, **viv))}
    assert want in got, sorted(got)


@pytest.mark.parametrize("ref,want", [("qukfY", "kartum"), pytest.param("BvAdi_01_1137", "gantum", marks=pytest.mark.xfail(reason="stem stops before tripāḍī (gamtum); avyaya sup-luk 2.4.82 for kṛt avyayas not built", strict=True)), ("RIY", "netum"), ("BvAdi_01_0381", "paWitum"),
                                     ("BvAdi_01_1092", "Srotum")])
def test_tumun_stem(ref, want):
    """तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम् (भविष्यति): the stem is an avyaya (1.1.39 kṛnmejantaḥ); explore() takes tumun and ṇvul as its two readings."""
    outs = set()
    for b in explore(lambda: _stem_state(ref)):
        outs.add(b.surface_slp1)
    assert want in outs, sorted(outs)


def _stem_state(ref):
    from engine.state import State
    stem, tags, multi = derive_krdanta_stem(ref, kala="Bavizyat", kriyArTA="kriyArTA")
    s = State(terms=[])
    from pipelines.subanta import build_initial_state
    s = build_initial_state(stem, 1, 1, "pulliṅga", derived_pratipadika=True)
    s.terms = s.terms[:1]
    s.meta["vikalpa_multi"] = multi
    return s
