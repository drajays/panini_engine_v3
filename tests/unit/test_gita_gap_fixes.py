"""Regressions for the Gītā gap loop (docs/GITA_GAP_PLAN.md): each case is a form the reader found wrong."""
import pytest

from pipelines.subanta import derive as sub
from pipelines.tinanta import derive as tin


def test_ayogavaha_stems_keep_M_and_H():
    assert sub("saMSaya", 1, 1).flat_dev() == "संशयः" and sub("duHKa", 2, 1, linga="napuṃsaka").flat_dev() == "दुःखम्"


def test_strI_i_u_stems_take_ya_not_na_7_3_120_astriyam():
    assert [sub(s, 3, 1, linga="strīliṅga").flat_dev() for s in ("mati", "Bakti", "Denu", "budDi")] == \
        ["मत्या", "भक्त्या", "धेन्वा", "बुद्ध्या"]
    assert sub("hari", 3, 1).flat_dev() == "हरिणा"            # masculine keeps nā


IN_HAN = {"yogin": ["योगी", "योगिनौ", "योगिनः", "योगिनम्", "योगिना", "हे योगिन्"],
          "vftrahan": ["वृत्रहा", "वृत्रहणौ", "वृत्रहणः", "वृत्रहणम्"],
          "pUzan": ["पूषा", "पूषणौ", "पूषणः", "पूषणम्"], "aryaman": ["अर्यमा", "अर्यमणौ", "अर्यमणः", "अर्यमणम्"]}


@pytest.mark.parametrize("stem", ["yogin", "vftrahan", "pUzan", "aryaman"])
def test_in_han_pusan_aryaman_6_4_12_13(stem):
    want = IN_HAN[stem]
    got = [sub(stem, v, n).flat_dev() for v, n in [(1, 1), (1, 2), (1, 3), (2, 1)]]
    assert got == want[:4]


def test_in_stem_vocative_and_neuter():
    assert sub("yogin", 8, 1).flat_dev() == "योगिन्"
    assert [sub("dehin", v, n, linga="napuṃsaka").flat_dev() for v, n in [(1, 1), (1, 2), (1, 3)]] == ["देहि", "देहिनी", "देहीनि"]


def _row(d, lak, pr="kartari", **kw):
    return [tin(d, lak, pr, p, n, **kw).flat_dev() for p in (1, 2, 3) for n in (1, 2, 3)]


def test_adadi_ya_and_as():
    assert _row("Adadi_02_0044", "laT")[-1] == "यान्ति"                       # या + अन्ति: 6.1.101
    assert _row("Adadi_02_0011", "laT")[-1] == "आसते"                          # ātmanepada 3pl: 7.1.5 / 7.1.3
    assert _row("Adadi_02_0060", "liG") == ["स्याम्", "स्याव", "स्याम", "स्याः", "स्यातम्", "स्यात", "स्यात्", "स्याताम्", "स्युः"]


def test_jYA_jan_7_3_79():
    assert _row("kryAdi_09_0043", "laT")[0::3] == ["जानामि", "जानासि", "जानाति"]
    assert tin("kryAdi_09_0043", "laT", "kartari", 3, 1).flat_dev() == "जानाति"
    assert tin("kryAdi_09_0043", "loT", "kartari", 2, 1).flat_dev() == "जानीहि"
    assert [tin("divAdi_04_0044", "laT", "kartari", 3, n).flat_dev() for n in (1, 2, 3)] == ["जायते", "जायेते", "जायन्ते"]


@pytest.mark.parametrize("d,lak,up,want", [
    ("svAdi_05_0016", "laT", ["ava"], "अवाप्नोति"), ("Adadi_02_0011", "laT", ["upa"], "उपासते"),
    ("Adadi_02_0011", "laT", ["pari", "upa"], "पर्युपासते"),
    ("kryAdi_09_0043", "laT", ["aBi"], "अभिजानाति"), ("kryAdi_09_0043", "laT", ["sam"], "सञ्जानाति"),
    ("divAdi_04_0044", "laT", ["sam"], "सञ्जायते"), ("Adadi_02_0044", "laT", ["sam"], "संयाति"),
])
def test_upasarga_junction_and_sam_anusvara(d, lak, up, want):
    assert tin(d, lak, "kartari", 3, 3 if d.startswith("Adadi_02_0011") else 1, upasargas=up).flat_dev() == want


def test_vid_lat_3_4_83_both_readings():
    from engine.vikalpa import choose
    cells = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    d = "Adadi_02_0059"
    with choose({"3.4.83": False}):
        assert [tin(d, "laT", "kartari", p, n).flat_dev() for p, n in cells] == \
            ["वेद्मि", "विद्वः", "विद्मः", "वेत्सि", "वित्थः", "वित्थ", "वेत्ति", "वित्तः", "विदन्ति"]
    with choose({"3.4.83": True}):   # ṇalādi: ṇal/ṭhal replace pit tip/sip/mip (guṇa), atus/aṭhus/us/a/va/ma are kṅit
        assert [tin(d, "laT", "kartari", p, n).flat_dev() for p, n in cells] == \
            ["वेद", "विद्व", "विद्म", "वेत्थ", "विदथुः", "विद", "वेद", "विदतुः", "विदुः"]


def test_3_4_83_only_for_vid_jnane():
    from engine.vikalpa import choose, explore
    run = lambda: tin("Adadi_02_0044", "laT", "kartari", 3, 3)           # yA: not vid
    assert [b.surface_dev for b in explore(run)] == ["यान्ति"]
    assert {b.surface_dev for b in explore(lambda: tin("Adadi_02_0059", "laT", "kartari", 3, 3))} == {"विदन्ति", "विदुः"}
