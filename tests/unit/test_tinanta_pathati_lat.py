"""
tests/unit/test_tinanta_pathati_lat.py

Glass-box gold tests for पठँ (paṭh, gaṇa 1 parasmaipada) + लट् — all 9 cells.

Derivation (3sg): पठँ [1.3.2 anunāsika-it] → पठ् [1.3.9 lopa]
  → पठ् + तिप् [3.4.78] → पठ् + ति [1.3.3/1.3.9 p-it lopa]
  → [3.4.113] → पठ् + शप् + ति [3.1.68] → पठ् + अ + ति [1.3.3/1.3.8/1.3.9]
  → [1.4.13/1.4.14] → पठति

Key: dhātu is consonant-final (ṭh); no guṇa fires (no IK upadhā vowel);
     śap-a follows W (ṭh) directly; no sandhi needed.
Input key: 'paW' (raw post-IT-lopa form of upadeśa 'paWa~' = पठँ).
Upadeśa 'paWa~' has anunaasika-seṭ IT; the engine's 1.3.12 path for
seṭ dhātus is a known open issue — tests use post-lopa form to
exercise the laṭ/laṅ/etc. spine without the IT-pada interaction.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_LAT_EXPECTED = {
    (3, 1): "पठति",   (3, 2): "पठतः",   (3, 3): "पठन्ति",
    (2, 1): "पठसि",   (2, 2): "पठथः",   (2, 3): "पठथ",
    (1, 1): "पठामि",  (1, 2): "पठावः",  (1, 3): "पठामः",
}

_PURUSHA = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA  = {1: "एक",    2: "द्वि",   3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _LAT_EXPECTED.items()
])
def test_path_lat_form(purusha, vacana, expected):
    state = derive("paW", "laT", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"पठ् लट् {_PURUSHA[purusha]}पुरुष {_VACANA[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_path_1_3_2_anunasika_it():
    """1.3.2 (anunaasika IT on final a~) must fire for the dhātu IT-lopa."""
    state = derive("paW", "laT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "1.3.2" in applied, "1.3.2 (anunāsika IT) must fire for पठँ"


def test_path_1_3_9_it_lopa_dhatu():
    """1.3.9 must drop the anunāsika 'a' of पठँ → पठ् (form change: paWa → paW)."""
    state = derive("paW", "laT", "kartari", 3, 1)
    # Find the 1.3.9 step that changes the dhātu form
    dhatu_lopa = [
        t for t in state.trace
        if t.get("sutra_id") == "1.3.9" and
           t.get("form_before", "").endswith("Wa") and
           t.get("form_after", "").endswith("W")
    ]
    assert dhatu_lopa, "1.3.9 must drop anunāsika 'a' of पठँ → पठ्"


def test_path_sap_vikarana():
    """3.1.68 (śap vikaraṇa) must fire for gaṇa-1 dhātu पठ्."""
    state = derive("paW", "laT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.1.68" in applied, "3.1.68 (śap) must fire for पठ् laT"


def test_path_no_guna():
    """7.3.84 (guṇa) must NOT fire — पठ् has no IK upadhā vowel ('a' is not IK)."""
    state = derive("paW", "laT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.84" not in applied, "7.3.84 (guṇa) must NOT fire for पठ् (non-IK stem)"


def test_path_3_4_113_sarvadhatu():
    """3.4.113 (tiṅ/śit is sārvadhatuka) must fire."""
    state = derive("paW", "laT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.113" in applied, "3.4.113 (sārvadhatuka) must fire for पठ् laT"


def test_path_other_lakaras():
    """Key forms across implemented lakāras."""
    cases = [
        ("loT", 3, 1, "पठतु"),
        ("laG", 3, 1, "अपठत्"),
        ("liG", 3, 1, "पठेत्"),
        ("lRT", 3, 1, "पठिष्यति"),
        ("lRG", 3, 1, "अपठिष्यत्"),
        ("AsIrliG", 3, 1, "पठ्यात्"),
    ]
    for lakara, pu, va, expected in cases:
        state = derive("paW", lakara, "kartari", pu, va)
        assert state.flat_dev() == expected, (
            f"पठ् {lakara} ({pu},{va}): got {state.flat_dev()!r}, expected {expected!r}"
        )


def test_bhu_unaffected():
    """bhū forms must remain correct after the paṭh lookup fix."""
    from pipelines.tinanta import derive_bhavati, derive_bhavisyati, derive_abhavat
    assert derive_bhavati().flat_dev()    == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
    assert derive_abhavat().flat_dev()    == "अभवत्"
