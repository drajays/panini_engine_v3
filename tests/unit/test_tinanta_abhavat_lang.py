"""
tests/unit/test_tinanta_abhavat_lang.py

Glass-box gold tests for भू + लङ् parasmaipada — all 9 cells.
Verifies the laṅ pipeline: śap vikaraṇa + aṭ augment (6.4.71) +
3.4.100/3.4.101/3.4.99 tiṅ substitutions + tripāḍī.
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_LAG_EXPECTED = {
    (3, 1): "अभवत्",
    (3, 2): "अभवताम्",
    (3, 3): "अभवन्",
    (2, 1): "अभवः",
    (2, 2): "अभवतम्",
    (2, 3): "अभवत",
    (1, 1): "अभवम्",
    (1, 2): "अभवाव",
    (1, 3): "अभवाम",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_LAG_EXPECTED.items()
])
def test_bhu_lag_form(purusha, vacana, expected):
    state = derive("BU", "laG", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू लङ् {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_lag_3sg_at_augment():
    """6.4.71 must fire (aṭ inserted into dhātu) for 3sg."""
    state = derive("BU", "laG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.4.71" in applied, "6.4.71 (aṭ augment) must fire for laṅ"


def test_bhu_lag_3sg_jal_jas_and_car():
    """3sg: 8.2.39 (t→d) and 8.4.56 (d→t) must both fire."""
    state = derive("BU", "laG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "8.2.39" in applied, "8.2.39 (t→d) must fire for laṅ 3sg"
    assert "8.4.56" in applied, "8.4.56 (d→t at avasāna) must fire for laṅ 3sg"


def test_bhu_lag_3du_3_4_101_tas_tam():
    """3du: 3.4.101 (tas→tām) must fire."""
    state = derive("BU", "laG", "kartari", 3, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (tas→tām) must fire for laṅ 3du"


def test_bhu_lag_3pl_itasca_and_jho_anta():
    """3pl: 3.4.100 (jhi→jh) and 7.1.3 (jh→ant) must fire."""
    state = derive("BU", "laG", "kartari", 3, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.100" in applied, "3.4.100 (jhi→jh) must fire for laṅ 3pl"
    assert "7.1.3" in applied, "7.1.3 (jh→ant) must fire for laṅ 3pl"


def test_bhu_lag_1sg_3_4_101_mi_am():
    """1sg: 3.4.101 (mi→am from mip) must fire."""
    state = derive("BU", "laG", "kartari", 1, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (mi→am) must fire for laṅ 1sg"


def test_bhu_lag_1du_diirgha_yañi():
    """1du: 7.3.101 (ā before v of 'v' tiṅ) must fire."""
    state = derive("BU", "laG", "kartari", 1, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.101" in applied, "7.3.101 (ā before yañ) must fire for laṅ 1du"
    assert "3.4.99" in applied, "3.4.99 (vas→v) must fire for laṅ 1du"


def test_bhu_lag_existing_unaffected():
    """laṭ/liṭ/lṛṭ forms must remain correct after laṅ implementation."""
    from pipelines.tinanta import derive_bhavati, derive_bhavisyati
    assert derive_bhavati().flat_dev() == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
