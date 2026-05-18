"""
tests/unit/test_tinanta_bhavatu_lot.py

Glass-box gold tests for भू + लोँट् (loṭ / imperative) parasmaipada — all 9 cells.
Sūtra chain: 3.3.162 → 3.4.78(laT ādeśas) → 3.4.113(sārvadhatuka) → śap
             → 3.4.89(mi→ni) → 3.4.101(tas→tām) → 3.4.87(sip→hi) → 7.1.3(jhi→anti)
             → 3.4.86(i→u: ti→tu, anti→antu) → 3.4.99(vas→va, mas→ma)
             → 6.4.105(hi-lopa) → 7.3.101(dīrgha before yañ) → 7.3.84(guṇa) → 6.1.78
Key: no aṭ (no 6.4.71); no 3.4.100 (loṭ retains 'i' — 3.4.86 converts to 'u').
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_LOT_EXPECTED = {
    (3, 1): "भवतु",
    (3, 2): "भवताम्",
    (3, 3): "भवन्तु",
    (2, 1): "भव",
    (2, 2): "भवतम्",
    (2, 3): "भवत",
    (1, 1): "भवानि",
    (1, 2): "भवाव",
    (1, 3): "भवाम",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_LOT_EXPECTED.items()
])
def test_bhu_lot_form(purusha, vacana, expected):
    state = derive("BU", "loT", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू लोँट् {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_lot_3sg_3486_iu():
    """3.4.86 (i→u) must fire for 3sg: tip→ti→tu."""
    state = derive("BU", "loT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.86" in applied, "3.4.86 (i→u) must fire for loṭ 3sg"


def test_bhu_lot_3pl_7_1_3():
    """7.1.3 (jhi→anti) and 3.4.86 (anti→antu) must fire for 3pl."""
    state = derive("BU", "loT", "kartari", 3, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.1.3"  in applied, "7.1.3 (jhi→anti) must fire for loṭ 3pl"
    assert "3.4.86" in applied, "3.4.86 (anti→antu) must fire for loṭ 3pl"


def test_bhu_lot_2sg_3487_sip_hi():
    """3.4.87 (sip→hi) must fire for 2sg."""
    state = derive("BU", "loT", "kartari", 2, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.87" in applied, "3.4.87 (sip→hi) must fire for loṭ 2sg"


def test_bhu_lot_2sg_6_4_105_hi_lopa():
    """6.4.105 (atō heḥ — hi deleted after a) must fire for 2sg."""
    state = derive("BU", "loT", "kartari", 2, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.4.105" in applied, "6.4.105 (hi-lopa) must fire for loṭ 2sg"


def test_bhu_lot_2sg_no_at():
    """6.4.71 (aṭ) must NOT fire — loṭ has no past-tense augment."""
    state = derive("BU", "loT", "kartari", 2, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.4.71" not in applied, "6.4.71 (aṭ) must NOT fire for loṭ"


def test_bhu_lot_3du_3101():
    """3.4.101 (tas→tām) must fire for 3du."""
    state = derive("BU", "loT", "kartari", 3, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (tas→tām) must fire for loṭ 3du"


def test_bhu_lot_1sg_3489_mi_ni():
    """3.4.89 (mi→ni) must fire for 1sg."""
    state = derive("BU", "loT", "kartari", 1, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.89" in applied, "3.4.89 (mi→ni) must fire for loṭ 1sg"


def test_bhu_lot_1sg_dirgha():
    """7.3.101 (dīrgha before yañ n) must fire for 1sg: a→ā before ni."""
    state = derive("BU", "loT", "kartari", 1, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.101" in applied, "7.3.101 (dīrgha) must fire for loṭ 1sg"


def test_bhu_lot_1du_3499_s_lopa():
    """3.4.99 (vas→va s-lopa) must fire for 1du."""
    state = derive("BU", "loT", "kartari", 1, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.99" in applied, "3.4.99 (s-lopa) must fire for loṭ 1du"


def test_bhu_lot_guna():
    """7.3.84 (guṇa) must fire — śap is sārvadhatuka."""
    state = derive("BU", "loT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.84" in applied, "7.3.84 (guṇa) must fire for loṭ"


def test_bhu_lot_no_3_4_100():
    """3.4.100 (itaś ca, i-lopa) must NOT fire — loṭ uses 3.4.86 instead."""
    state = derive("BU", "loT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.100" not in applied, "3.4.100 (itaś ca) must NOT fire for loṭ"


def test_bhu_lot_existing_unaffected():
    """All prior lakāra forms must remain correct."""
    from pipelines.tinanta import (
        derive_bhavati, derive_bhavisyati, derive_abhavat,
        derive_bhavet, derive_bhuyat, derive_abhut, derive_abhavisyat
    )
    assert derive_bhavati().flat_dev()    == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
    assert derive_abhavat().flat_dev()    == "अभवत्"
    assert derive_bhavet().flat_dev()     == "भवेत्"
    assert derive_bhuyat().flat_dev()     == "भूयात्"
    assert derive_abhut().flat_dev()      == "अभूत्"
    assert derive_abhavisyat().flat_dev() == "अभविष्यत्"
