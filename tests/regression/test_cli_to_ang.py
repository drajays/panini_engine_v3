"""cli → aṅ in luṅ (3.1.52–3.1.58) and the rules that follow it (6.4.34 शास इदङ्हलोः, 7.4.16 ऋदृशोऽङि गुणः) — Kāśikā forms.
Optional rules (3.1.54, 3.1.57, 3.1.58) take either branch through engine.vikalpa.choose.
Vidyut verdicts: for सृ / शास् / ऋ Vidyut lists asArzIt / nothing / ArzIt; Kāśikā 3.1.56 (असरत्, अशिषत्, आरत्) decides (Art. 22: grantha over Vidyut)."""
import pytest

from engine.vikalpa import choose
from pipelines.tinanta import derive

NITYA = [   # (dhātupāṭha id, pada, (purusha, vacana), form, sūtra)
    ("02.0058", "parasmai", (3, 1), "avocat", "3.1.52"),     # वच्
    ("02.0058", "parasmai", (3, 3), "avocan", "3.1.52"),
    ("06.0169", "parasmai", (3, 1), "alipat", "3.1.53"),     # लिप्
    ("06.0170", "parasmai", (3, 1), "asicat", "3.1.53"),     # सिच्
    ("01.1163", "parasmai", (3, 1), "ahvat", "3.1.53"),      # ह्वेञ्
    ("01.1085", "parasmai", (3, 1), "asarat", "3.1.56"),     # सृ  (7.4.16)
    ("01.1086", "parasmai", (3, 1), "Arat", "3.1.56"),       # ऋ
    ("02.0070", "parasmai", (3, 1), "aSizat", "3.1.56"),     # शास्  (6.4.34, 8.3.60)
    ("02.0070", "parasmai", (3, 3), "aSizan", "3.1.56"),
]


@pytest.mark.parametrize("ref,pada,cell,form,sutra", NITYA)
def test_ang_nitya(ref, pada, cell, form, sutra):
    assert derive(ref, "luG", "kartari", *cell, pada=pada).render() == form


VIKALPA = [   # (id, pada, cell, sutra, sic form, aṅ form)
    ("06.0169", "atmane", (3, 1), "3.1.54", "alipta", "alipata"),
    ("07.0002", "parasmai", (3, 1), "3.1.57", "aBEtsIt", "aBidat"),      # भिदिर्
    ("01.1143", "parasmai", (3, 3), "3.1.57", "adrAkzuH", "adarSan"),    # दृशिर्
    ("01.0222", "parasmai", (3, 1), "3.1.58", "amrocIt", "amrucat"),     # म्रुचु
    ("01.0225", "parasmai", (3, 1), "3.1.58", "aglocIt", "aglucat"),     # ग्लुचु
]


@pytest.mark.parametrize("ref,pada,cell,sutra,sic,ang", VIKALPA)
def test_ang_vikalpa_both_readings(ref, pada, cell, sutra, sic, ang):
    assert derive(ref, "luG", "kartari", *cell, pada=pada).render() == sic
    with choose({sutra: True}):
        assert derive(ref, "luG", "kartari", *cell, pada=pada).render() == ang


def test_other_roots_keep_sic():
    assert derive("01.0001", "luG", "kartari", 3, 1).render() == "aBUt"
    assert derive("01.0034", "luG", "kartari", 3, 1, pada="parasmai").render().endswith("It")     # a sic root: no aṅ


def test_asu_sasu_icchayam_is_aashas_not_sas():
    """आङः शासु इच्छायाम् (02.0012) is the dhātu आशास्: 6.4.34 does not touch it (आशास्ते), while अनुशिष्टौ शास् gives शिष्टः."""
    assert derive("02.0012", "laT", "kartari", 3, 1, pada="atmane").render() == "SAste"
    assert derive("02.0070", "laT", "kartari", 3, 2).render() == "SizwaH"
