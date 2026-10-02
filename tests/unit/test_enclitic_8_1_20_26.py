"""8.1.20–26 — yuṣmad/asmad ādeśas in a sentence. Examples: Kāśikā (as quoted in sutra_ref_out/8_1_2x.json)."""
import pytest

from pipelines.enclitic import derive_in_context as derive, derive_in_context_branches as branches

G = {"slp1": "grAmaH", "vibhakti": 1}
SEEING = {"slp1": "paSyati", "yukta": True, "paSyArTa": True, "AlocanArTa": True}   # ālocana: ādeśa stands
THINKING = {"slp1": "samIkzya", "yukta": True, "paSyArTa": True}                   # jñāna: 8.1.25 blocks
SAPURVA = [{"slp1": "grAme", "vibhakti": 7}, {"slp1": "kambalaH", "vibhakti": 1}]

CASES = [  # (stem, vibhakti, vacana, before, after, expected slp1)
    ("yuzmad", 6, 1, [G], [], "te"), ("asmad", 6, 1, [G], [], "me"),            # ग्रामस्ते स्वम् / ग्रामो मे स्वम् 8.1.22
    ("yuzmad", 4, 1, [G], [], "te"), ("asmad", 4, 1, [G], [], "me"),            # … दीयते — the मह्यम् → मे of the brief
    ("yuzmad", 6, 2, [G], [], "vAm"), ("asmad", 6, 2, [G], [], "nO"),           # ग्रामो वां स्वम् / नौ 8.1.20
    ("yuzmad", 4, 2, [G], [], "vAm"), ("asmad", 2, 2, [G], [], "nO"),
    ("yuzmad", 6, 3, [G], [], "vaH"), ("asmad", 6, 3, [G], [], "naH"),          # ग्रामो वः / नः स्वम् 8.1.21
    ("yuzmad", 4, 3, [G], [], "vaH"), ("asmad", 2, 3, [G], [], "naH"),
    ("yuzmad", 2, 1, [G], [SEEING], "tvA"), ("asmad", 2, 1, [G], [SEEING], "mA"),  # ग्रामस्त्वा पश्यति 8.1.23
    ("yuzmad", 6, 1, [], [], "tava"), ("asmad", 4, 1, [], [], "mahyam"),        # apādādau (8.1.18): pāda-initial
    ("yuzmad", 6, 1, [G], [{"slp1": "ca", "lexeme": "ca"}], "tava"),            # 8.1.24 ग्रामस्तव च स्वम्
    ("asmad", 6, 1, [G], [{"slp1": "eva", "lexeme": "eva"}], "mama"),
    ("yuzmad", 6, 1, [{"slp1": "grAmaSca", "vibhakti": 1}], [], "te"),          # 8.1.24 yuktayukte: no block
    ("yuzmad", 6, 1, [G], [THINKING], "tava"),                                  # 8.1.25 समीक्ष्य
    ("yuzmad", 3, 1, [G], [], "tvayA"), ("yuzmad", 3, 2, [G], [], "yuvAByAm"),  # tṛtīyā is not stha
]


@pytest.mark.parametrize("stem,v,n,before,after,want", CASES)
def test_enclitic(stem, v, n, before, after, want):
    assert derive(stem, v, n, before=before, after=after).flat_slp1() == want


def test_8_1_26_vibhasha_gives_both_readings():
    assert {b.surface_slp1 for b in branches("yuzmad", 6, 1, before=SAPURVA)} == {"te", "tava"}
    assert {b.surface_slp1 for b in branches("asmad", 6, 1, before=SAPURVA)} == {"me", "mama"}


def test_8_1_26_does_not_fire_without_sapurva():  # ग्रामस्ते: ādeśa is nitya
    assert [b.surface_slp1 for b in branches("yuzmad", 6, 1, before=[G])] == ["te"]


def test_brief_trace_mahyam_to_me_by_8_1_22():
    s = derive("asmad", 4, 1, before=[G])
    fired = [r["sutra_id"] for r in s.trace if r.get("status") == "APPLIED"]
    for sid in ("4.1.2", "1.3.8", "1.3.9", "7.1.28", "7.2.95", "6.1.97", "7.2.90", "6.1.107", "8.1.22"):
        assert sid in fired, sid
    assert fired.index("7.2.95") < fired.index("6.1.107") < fired.index("8.1.22")


def test_ordinary_forms_unchanged():
    from pipelines.asmad_subanta import derive_asmad
    assert derive_asmad(4, 1).flat_slp1() == "mahyam" and derive_asmad(6, 3).flat_slp1() == "asmAkam"
