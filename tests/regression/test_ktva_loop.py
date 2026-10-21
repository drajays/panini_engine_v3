"""Absolutives (ktvā) through the recipe-free loop: scheduler + vacuity filter + resolver from a dhātu and the
3.4.21 vivakṣā. Expected forms are Kāśikā udāharaṇas (3.4.21, 6.4.37, 7.2.11) and the corpus-gap words.

Shows 3.4.114 naming ktvā ārdhadhātuka (पठित्वा takes iṭ by 7.2.35), 7.2.10 (त्यक्त्वा, कृत्वा, गत्वा: anudātta
roots), 7.2.11 श्र्युकः किति (भूत्वा, श्रित्वा, युत्वा, लूत्वा, वृत्वा), 6.4.37 (गत्वा, यत्वा, रत्वा), and that a vikaraṇa
(रुधादि śnam) does not stand before a non-śit kṛt (भुक्त्वा). With an upasarga: 1.4.60 gati, 2.2.18 gati-samāsa before sup,
7.1.37 ल्यप् (प्रकृत्य, आगत्य, निशम्य).
"""
from __future__ import annotations

import pytest

import sutras  # noqa: F401
from engine import SUTRA_REGISTRY, apply_rule
from engine.state import Term
from engine.tape_init.krdanta import PURVAKALA_SAMANAKARTRKA
from phonology.varna import parse_slp1_upadesha_sequence
from pipelines.krdanta import build_dhatu_state
from tools.autonomy_report import run_autonomously

CASES = [
    ("BvAdi_01_0001", "BUtvA"),        # भूत्वा
    ("BvAdi_01_1137", "gatvA"),        # गत्वा
    ("BvAdi_01_1141", "tyaktvA"),      # त्यक्त्वा
    ("BvAdi_01_1143", "dfzwvA"),       # दृष्ट्वा
    ("qukfY", "kftvA"),                # कृत्वा
    ("BvAdi_01_0381", "paWitvA"),      # पठित्वा
    ("BvAdi_pA", "pItvA"),             # पीत्वा  (Kāśikā 3.4.21)
    ("ruDAdi_07_0017", "BuktvA"),      # भुक्त्वा (Kāśikā 3.4.21)
    ("BvAdi_01_1092", "SrutvA"),       # श्रुत्वा
    ("BvAdi_01_1044", "SritvA"),       # श्रित्वा (Kāśikā 7.2.11)
    ("Adadi_02_0027", "yutvA"),        # युत्वा
    ("lUY", "lUtvA"),                  # लूत्वा
    ("svAdi_05_0008", "vftvA"),        # वृत्वा
    ("BvAdi_01_1031", "yatvA"),        # यत्वा (Kāśikā 6.4.37)
    ("BvAdi_01_0989", "ratvA"),        # रत्वा
    ("Adadi_02_0047", "snAtvA"),       # स्नात्वा (Kāśikā 3.4.21)
]

GAPS = [
    pytest.param("BvAdi_01_1124", "tIrtvA", marks=pytest.mark.xfail(strict=True,
                 reason="7.1.100 ॠत इद्धातोः + hali dīrgha not reached on a kṛt tape (gives tFtvA)")),
    pytest.param("JuhotyAdi_03_0010", "dattvA", marks=pytest.mark.xfail(strict=True,
                 reason="7.4.46 दो दद्घोः loses to 6.4.66 घुमास्था… (gives dItvA)")),
]


def _derive(ref: str, expected: str):
    s = build_dhatu_state(ref, **PURVAKALA_SAMANAKARTRKA)
    s.phase = "upadesha"
    return run_autonomously(s, expected, ref, 150)


@pytest.mark.parametrize("ref,expected", CASES + GAPS)
def test_ktva_through_the_loop(ref, expected):
    run = _derive(ref, expected)
    assert run.surface == expected, [s[0] for s in run.steps]


LYAP = [
    ("pra", "qukfY", "prakftya"),          # प्रकृत्य (Kāśikā 7.1.37; Padamañjarī: क्त्वा → कुगतिप्रादयः → ल्यप् → तुक्)
    ("pra", "hfY", "prahftya"),            # प्रहृत्य (Kāśikā 7.1.37)
    ("A", "BvAdi_01_1137", "Agatya"),      # आगत्य (Kāśikā 6.4.38)
    ("pra", "BvAdi_01_0381", "prapaWya"),  # प्रपठ्य (ashtadhyayi.com prakriyā under 1.1.56)
    ("ni", "Samu~", "niSamya"),            # निशम्य (corpus-gap word)
    ("vi", "BvAdi_01_1143", "vidfSya"),
]


@pytest.mark.parametrize("upasarga,ref,expected", LYAP)
def test_lyap_through_the_loop(upasarga, ref, expected):
    """1.4.59 upasarga → 1.4.60 gati → 2.2.18 gati-samāsa before sup → 7.1.37 ल्यप्, no recipe flag."""
    s = build_dhatu_state(ref, **PURVAKALA_SAMANAKARTRKA)
    s.terms.insert(0, Term(kind="upasarga", varnas=list(parse_slp1_upadesha_sequence(upasarga)), tags=set(),
                           meta={"upadesha_slp1": upasarga}))
    s.phase = "upadesha"
    run = run_autonomously(s, expected, ref, 200)
    ids = [step[0] for step in run.steps]
    assert run.surface == expected, ids
    assert ids.index("2.2.18") < ids.index("7.1.37")


def test_lyap_pratyudaharana_nan_purva():
    """अनञ्पूर्व इति किम्? अकृत्वा — a nañ pūrvapada keeps ktvā."""
    s = build_dhatu_state("qukfY", **PURVAKALA_SAMANAKARTRKA)
    s.terms.insert(0, Term(kind="nipata", varnas=list(parse_slp1_upadesha_sequence("a")),
                           tags={"samasa_member", "samasa_purvapada", "tatpurusha"}, meta={"upadesha_slp1": "naY"}))
    s = apply_rule("3.4.21", s)
    assert not SUTRA_REGISTRY["7.1.37"].cond(s)


def test_no_ktva_without_the_vivaksha():
    s = build_dhatu_state("BvAdi_01_0001")
    s.phase = "upadesha"
    run = run_autonomously(s, "BU", "bare", 150)
    assert "3.4.21" not in [step[0] for step in run.steps]
