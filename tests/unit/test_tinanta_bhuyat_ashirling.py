"""
tests/unit/test_tinanta_bhuyat_ashirling.py

Glass-box gold tests for भू + आशीर्-लिँङ् (āśīr-liṅ / benedictive) parasmaipada — all 9 cells.
Verifies: 3.3.173 → 3.4.104(yāsuṭ KIT) → 3.4.107(suṭ) → 8.2.29(s-lopa) → bhūyāt paradigm.
No guṇa on dhātu (kit yāsuṭ → 1.1.5 blocks), no śap vikaraṇa (ārdhadhātuka).
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_ASHIR_EXPECTED = {
    (3, 1): "भूयात्",
    (3, 2): "भूयास्ताम्",
    (3, 3): "भूयासुः",
    (2, 1): "भूयाः",
    (2, 2): "भूयास्तम्",
    (2, 3): "भूयास्त",
    (1, 1): "भूयासम्",
    (1, 2): "भूयास्व",
    (1, 3): "भूयास्म",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_ASHIR_EXPECTED.items()
])
def test_bhu_ashir_form(purusha, vacana, expected):
    state = derive("BU", "AsIrliG", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू आशीर्-लिँङ् {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_ashir_3sg_yasut_kit():
    """3.4.104 (kidāśiṣi yāsuṭ) must fire for 3sg."""
    state = derive("BU", "AsIrliG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.104" in applied, "3.4.104 (kidāśiṣi yāsuṭ) must fire for āśīr-liṅ 3sg"


def test_bhu_ashir_3sg_suw():
    """3.4.107 (suṭ) must fire for 3sg (t-initial tiṅ)."""
    state = derive("BU", "AsIrliG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.107" in applied, "3.4.107 (suṭ) must fire for āśīr-liṅ 3sg"


def test_bhu_ashir_3sg_8229():
    """8.2.29 (saṃyoga s-lopa) must fire for 3sg."""
    state = derive("BU", "AsIrliG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "8.2.29" in applied, "8.2.29 (saṃyoga s-lopa) must fire for āśīr-liṅ 3sg"


def test_bhu_ashir_no_guna():
    """7.3.84 (guṇa) must NOT fire — kit yāsuṭ blocks via 1.1.5."""
    state = derive("BU", "AsIrliG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.84" not in applied, "7.3.84 (guṇa) must NOT fire for āśīr-liṅ (bhūyāt not bhaveyāt)"


def test_bhu_ashir_3pl_3_4_108():
    """3.4.108 (jhi→jus) must fire for 3pl."""
    state = derive("BU", "AsIrliG", "kartari", 3, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.108" in applied, "3.4.108 (jhi→jus) must fire for āśīr-liṅ 3pl"


def test_bhu_ashir_2sg_6166():
    """6.1.66 (apṛkta-s lopa) must fire for 2sg."""
    state = derive("BU", "AsIrliG", "kartari", 2, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.1.66" in applied, "6.1.66 (apṛkta-s lopa) must fire for āśīr-liṅ 2sg"


def test_bhu_ashir_3du_3_4_101():
    """3.4.101 (tas→tām) must fire for 3du."""
    state = derive("BU", "AsIrliG", "kartari", 3, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (tas→tām) must fire for āśīr-liṅ 3du"


def test_bhu_ashir_existing_unaffected():
    """Existing laṭ/lṛṭ/laṅ/liṅ forms must remain correct."""
    from pipelines.tinanta import (
        derive_bhavati, derive_bhavisyati, derive_abhavat, derive_bhavet
    )
    assert derive_bhavati().flat_dev()   == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
    assert derive_abhavat().flat_dev()   == "अभवत्"
    assert derive_bhavet().flat_dev()    == "भवेत्"
