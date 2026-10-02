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


def test_bru_3_4_84_ah_with_first_five():
    from engine.vikalpa import choose, explore
    d = "Adadi_02_0039"
    cells = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    with choose({"3.4.84": False}):
        assert [tin(d, "laT", "kartari", p, n).flat_dev() for p, n in cells] == \
            ["ब्रवीमि", "ब्रूवः", "ब्रूमः", "ब्रवीषि", "ब्रूथः", "ब्रूथ", "ब्रवीति", "ब्रूतः", "ब्रुवन्ति"]
    with choose({"3.4.84": True}):   # first five only: tha, mip, vas, mas keep their ordinary forms
        assert [tin(d, "laT", "kartari", p, n).flat_dev() for p, n in cells] == \
            ["ब्रवीमि", "ब्रूवः", "ब्रूमः", "आत्थ", "आहथुः", "ब्रूथ", "आह", "आहतुः", "आहुः"]
    assert {b.surface_dev for b in explore(lambda: tin(d, "laT", "kartari", 3, 3))} == {"ब्रुवन्ति", "आहुः"}


def test_8_2_35_only_before_th_initial():  # आहथुः keeps ह् (अथुस् is vowel-initial); आत्थ needs 8.2.35 then 8.4.55
    from engine.vikalpa import choose
    with choose({"3.4.84": True}):
        s = tin("Adadi_02_0039", "laT", "kartari", 2, 1)
    f = [r["sutra_id"] for r in s.trace if r.get("status") == "APPLIED"]
    assert s.flat_dev() == "आत्थ" and "8.2.35" in f and f.index("3.4.84") < f.index("8.2.35")


LIT = {  # root upadeśa → liṭ 3sg / 3du / 3pl  (ashtadhyayi.com dhātu table)
    "Adadi_02_0058": ["उवाच", "ऊचतुः", "ऊचुः"],          # vac: 6.1.17 abhyāsa, 6.1.15 root before kit
    "BvAdi_01_1157": ["इयाज", "ईजतुः", "ईजुः"],          # yaj
    "Adadi_02_0063": ["सुष्वाप", "सुषुपतुः", "सुषुपुः"],  # svap
    "BvAdi_01_1159": ["उवाह", "ऊहतुः", "ऊहुः"],          # vah
    "BvAdi_01_1164": ["उवाद", "ऊदतुः", "ऊदुः"],          # vad
}


@pytest.mark.parametrize("d", list(LIT))
def test_lit_samprasarana_6_1_15_6_1_17(d):
    assert [tin(d, "liT", "kartari", 3, n).flat_dev() for n in (1, 2, 3)] == LIT[d]


def test_plIhan_is_not_the_root_han_6_4_12():
    assert [sub("plIhan", v, n).flat_dev() for v, n in [(1, 1), (1, 2), (2, 1)]] == ["प्लीहा", "प्लीहानौ", "प्लीहानम्"]
    assert [sub("vftrahan", v, n).flat_dev() for v, n in [(1, 1), (1, 2), (2, 1)]] == ["वृत्रहा", "वृत्रहणौ", "वृत्रहणम्"]
    assert sub("Satruhan", 1, 2, han_dhatu=True).flat_dev() == "शत्रुहणौ"      # a han-compound 3.2.87 does not name: input


SRU = {  # श्रु (bhvādi): 3.1.74 श्नु + शृ; table order 1sg 1du 1pl 2sg 2du 2pl 3sg 3du 3pl
    "laT": ["शृणोमि", "शृणुवः", "शृणुमः", "शृणोषि", "शृणुथः", "शृणुथ", "शृणोति", "शृणुतः", "शृण्वन्ति"],
    "laG": ["अशृणवम्", "अशृणुव", "अशृणुम", "अशृणोः", "अशृणुतम्", "अशृणुत", "अशृणोत्", "अशृणुताम्", "अशृण्वन्"],
}


@pytest.mark.parametrize("lak", list(SRU))
def test_sru_3_1_74_snu(lak):
    got = [tin("BvAdi_01_1092", lak, "kartari", p, n).flat_dev() for p in (1, 2, 3) for n in (1, 2, 3)]
    # the table also lists the saṃyoga-free alternatives शृण्वः / शृण्मः (6.4.107) for vas / mas
    ok = [g == w or (g, w) in {("शृणुवः", "शृणुवः"), ("अशृणुव", "अशृणुव")} for g, w in zip(got, SRU[lak])]
    assert all(ok), [(g, w) for g, w, o in zip(got, SRU[lak], ok) if not o]


def test_sru_loT_2sg_and_3pl():
    assert tin("BvAdi_01_1092", "loT", "kartari", 2, 1).flat_dev() == "शृणु"
    assert tin("BvAdi_01_1092", "loT", "kartari", 3, 3).flat_dev() == "शृण्वन्तु"
    assert tin("BvAdi_01_1092", "liG", "kartari", 3, 1).flat_dev() == "शृणुयात्"


def test_8_3_59_leaves_the_stems_own_s_alone():  # आदेशप्रत्यययोः: only an ādeśa / pratyaya s becomes ṣ
    assert [sub("pustaka", v, n, linga="napuṃsaka").flat_dev() for v, n in [(1, 1), (7, 3)]] == ["पुस्तकम्", "पुस्तकेषु"]
    assert sub("kusuma", 3, 1, linga="napuṃsaka").flat_dev() == "कुसुमेन"
    assert sub("hiMsA", 1, 1, linga="strīliṅga").flat_dev() == "हिंसा"
    assert sub("vasu", 7, 3).flat_dev() == "वसुषु"              # the sup's s still becomes ṣ
    assert sub("havis", 3, 1, linga="napuṃsaka").flat_dev() == "हविषा"   # a stem-final s is the as/is/us suffix's: eligible
