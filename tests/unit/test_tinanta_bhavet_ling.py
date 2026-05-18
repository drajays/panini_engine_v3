"""
tests/unit/test_tinanta_bhavet_ling.py

Glass-box gold tests for भू + लिँङ् (vidhi-liṅ / optative) parasmaipada — all 9 cells.
Verifies: 3.3.161 → 3.4.103(yāsuṭ) → 7.2.79 → 7.2.80 → 6.1.66 → 6.1.87(e) → 7.3.84.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_LIG_EXPECTED = {
    (3, 1): "भवेत्",
    (3, 2): "भवेताम्",
    (3, 3): "भवेयुः",
    (2, 1): "भवेः",
    (2, 2): "भवेतम्",
    (2, 3): "भवेत",
    (1, 1): "भवेयम्",
    (1, 2): "भवेव",
    (1, 3): "भवेम",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_LIG_EXPECTED.items()
])
def test_bhu_lig_form(purusha, vacana, expected):
    state = derive("BU", "liG", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू लिँङ् {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_lig_3sg_yasut_inserted():
    """3.4.103 must fire (yāsuṭ inserted) for 3sg."""
    state = derive("BU", "liG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.103" in applied, "3.4.103 (yāsuṭ) must fire for vidhi-liṅ 3sg"


def test_bhu_lig_3sg_7279_7280_6166():
    """7.2.79, 7.2.80, 6.1.66 must all fire for 3sg."""
    state = derive("BU", "liG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.2.79" in applied, "7.2.79 (yāsuṭ s-lopa) must fire for liṅ 3sg"
    assert "7.2.80" in applied, "7.2.80 (yā→iy) must fire for liṅ 3sg"
    assert "6.1.66" in applied, "6.1.66 (y-lopa before hal) must fire for liṅ 3sg"


def test_bhu_lig_3sg_guna():
    """7.3.84 (guṇa BU→Bo) must fire for 3sg."""
    state = derive("BU", "liG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.84" in applied, "7.3.84 (guṇa) must fire for liṅ 3sg"


def test_bhu_lig_3du_3_4_101():
    """3.4.101 (tas→tām) must fire for 3du."""
    state = derive("BU", "liG", "kartari", 3, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (tas→tām) must fire for liṅ 3du"


def test_bhu_lig_3pl_3_4_108():
    """3.4.108 (jhi→jus) must fire for 3pl."""
    state = derive("BU", "liG", "kartari", 3, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.108" in applied, "3.4.108 (jhi→jus) must fire for liṅ 3pl"


def test_bhu_lig_1sg_3_4_101_am():
    """3.4.101 (mi→am) must fire for 1sg."""
    state = derive("BU", "liG", "kartari", 1, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (mi→am) must fire for liṅ 1sg"


def test_bhu_lig_existing_unaffected():
    """laṭ/lṛṭ/laṅ forms must remain correct after liṅ implementation."""
    from pipelines.tinanta import derive_bhavati, derive_bhavisyati, derive_abhavat
    assert derive_bhavati().flat_dev() == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
    assert derive_abhavat().flat_dev() == "अभवत्"
