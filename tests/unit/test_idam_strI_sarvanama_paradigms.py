"""इदम् — all 63 cells (three liṅgas), and the feminine sarvanāmas (तद् एतद् किम् यद् सर्व अन्य).

Gold: the ashtadhyayi.com śabda-prakriyā for इदम् (7.2.108–113, 7.1.11, 7.3.105/114/116, 4.1.4 …). Forms are listed
in the test, not read at run time. The sūtra path of the key cells is asserted too.
"""
import pytest

from pipelines.subanta import derive

IDAM = {
    "pulliṅga": [["अयम्", "इमौ", "इमे"], ["इमम्", "इमौ", "इमान्"], ["अनेन", "आभ्याम्", "एभिः"], ["अस्मै", "आभ्याम्", "एभ्यः"],
                 ["अस्मात्", "आभ्याम्", "एभ्यः"], ["अस्य", "अनयोः", "एषाम्"], ["अस्मिन्", "अनयोः", "एषु"]],
    "strīliṅga": [["इयम्", "इमे", "इमाः"], ["इमाम्", "इमे", "इमाः"], ["अनया", "आभ्याम्", "आभिः"], ["अस्यै", "आभ्याम्", "आभ्यः"],
                  ["अस्याः", "आभ्याम्", "आभ्यः"], ["अस्याः", "अनयोः", "आसाम्"], ["अस्याम्", "अनयोः", "आसु"]],
    "napuṃsaka": [["इदम्", "इमे", "इमानि"], ["इदम्", "इमे", "इमानि"], ["अनेन", "आभ्याम्", "एभिः"], ["अस्मै", "आभ्याम्", "एभ्यः"],
                  ["अस्मात्", "आभ्याम्", "एभ्यः"], ["अस्य", "अनयोः", "एषाम्"], ["अस्मिन्", "अनयोः", "एषु"]],
}
CELLS = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (6, 2), (6, 3), (7, 1), (7, 3)]
FEM = {  # strī: 1-1 1-2 1-3 2-1 3-1 4-1 5-1 6-1 6-2 6-3 7-1 7-3
    "tad":   ["सा", "ते", "ताः", "ताम्", "तया", "तस्यै", "तस्याः", "तस्याः", "तयोः", "तासाम्", "तस्याम्", "तासु"],
    "etad":  ["एषा", "एते", "एताः", "एताम्", "एतया", "एतस्यै", "एतस्याः", "एतस्याः", "एतयोः", "एतासाम्", "एतस्याम्", "एतासु"],
    "kim":   ["का", "के", "काः", "काम्", "कया", "कस्यै", "कस्याः", "कस्याः", "कयोः", "कासाम्", "कस्याम्", "कासु"],
    "yad":   ["या", "ये", "याः", "याम्", "यया", "यस्यै", "यस्याः", "यस्याः", "ययोः", "यासाम्", "यस्याम्", "यासु"],
    "sarva": ["सर्वा", "सर्वे", "सर्वाः", "सर्वाम्", "सर्वया", "सर्वस्यै", "सर्वस्याः", "सर्वस्याः", "सर्वयोः", "सर्वासाम्", "सर्वस्याम्", "सर्वासु"],
    "anya":  ["अन्या", "अन्ये", "अन्याः", "अन्याम्", "अन्यया", "अन्यस्यै", "अन्यस्याः", "अन्यस्याः", "अन्ययोः", "अन्यासाम्", "अन्यस्याम्", "अन्यासु"],
}


@pytest.mark.parametrize("linga", list(IDAM))
def test_idam_63_cells(linga):
    got = [[derive("idam", v, n, linga=linga).flat_dev() for n in (1, 2, 3)] for v in range(1, 8)]
    assert got == IDAM[linga]


@pytest.mark.parametrize("stem", list(FEM))
def test_strI_sarvanama_paradigm(stem):
    assert [derive(stem, v, n, linga="strīliṅga").flat_dev() for v, n in CELLS] == FEM[stem]


def _fired(s):
    return [r["sutra_id"] for r in s.trace if r.get("status") == "APPLIED"]


def test_ayam_path():  # इदम्+सु: 7.2.108 (m stays, apavāda of 7.2.102) → 7.2.111 (id→ay) → 6.1.68
    f = _fired(derive("idam", 1, 1))
    assert f.index("7.2.108") < f.index("7.2.111") < f.index("6.1.68") and "7.2.102" not in f


def test_ebhih_7_1_11_blocks_7_1_9():  # इदम्+भिस्: 7.1.11 stops bhis→ais; 7.2.113; 7.3.103 → एभिः
    s = derive("idam", 3, 3)
    assert "7.1.9" not in _fired(s) and {"7.2.113", "7.3.103"} <= set(_fired(s))
    assert any(r["sutra_id"] == "7.1.9" and r.get("status") == "BLOCKED" for r in s.trace)


def test_iyam_7_2_110_for_strI():
    f = _fired(derive("idam", 1, 1, linga="strīliṅga"))
    assert "7.2.110" in f and "7.2.111" not in f


def test_anayA_path():  # strī ṭā: 4.1.4 → 7.2.112 (id→an) → 7.3.105 (ā→e) → 6.1.78
    f = _fired(derive("idam", 3, 1, linga="strīliṅga"))
    assert f.index("7.2.112") < f.index("7.3.105") < f.index("6.1.78")


def test_asyAm_path():  # strī ṅi: 7.3.116 (ṅi→ām) then 7.3.114 (syāṭ), 7.2.113
    f = _fired(derive("idam", 7, 1, linga="strīliṅga"))
    assert f.index("7.3.116") < f.index("7.3.114") < f.index("7.2.113")


def test_neuter_plural_is_shi_not_shI():  # तानि / इमानि: 7.1.20 is para to 7.1.17
    assert derive("tad", 1, 3, linga="napuṃsaka").flat_dev() == "तानि"


ANVADESHA = {  # 2-1 2-2 2-3 3-1 6-2 7-2 — एन (2.4.34), idam and etad alike
    "pulliṅga": ["एनम्", "एनौ", "एनान्", "एनेन", "एनयोः", "एनयोः"],
    "strīliṅga": ["एनाम्", "एने", "एनाः", "एनया", "एनयोः", "एनयोः"],
    "napuṃsaka": ["एनत्", "एने", "एनानि", "एनेन", "एनयोः"],
}


@pytest.mark.parametrize("stem", ["idam", "etad"])
@pytest.mark.parametrize("linga", list(ANVADESHA))
def test_anvadesha_ena_2_4_34(stem, linga):
    cells = [(2, 1), (2, 2), (2, 3), (3, 1), (6, 2), (7, 2)][: len(ANVADESHA[linga])]
    assert [derive(stem, v, n, linga=linga, anvadesha=True).flat_dev() for v, n in cells] == ANVADESHA[linga]


def test_ena_only_in_anvadesha_and_traced():
    assert derive("idam", 2, 1).flat_dev() == "इमम्"                         # no anvādeśa: ordinary idam
    assert "2.4.34" in _fired(derive("idam", 2, 1, anvadesha=True))
    assert derive("idam", 1, 1, anvadesha=True).flat_dev() == "अयम्"          # prathamā su is not in 2.4.34's list
