"""
tests/unit/test_tinanta_abhut_lung.py

Glass-box gold tests for भू + लुँङ् (luṅ / aorist) parasmaipada — all 9 cells.
Verifies: 3.2.110 → 3.1.43(cli) → 3.1.44(sic) → 2.4.77(sic-luk)
          → 6.4.71(aṭ) → 6.4.88(vuk) → 6.1.66(v-lopa) → abhūt paradigm.
Key: no guṇa (vuk intervenes), no śap (ārdhadhātuka/sicluk path).
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_LUG_EXPECTED = {
    (3, 1): "अभूत्",
    (3, 2): "अभूताम्",
    (3, 3): "अभूवन्",
    (2, 1): "अभूः",
    (2, 2): "अभूतम्",
    (2, 3): "अभूत",
    (1, 1): "अभूवम्",
    (1, 2): "अभूव",
    (1, 3): "अभूम",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_LUG_EXPECTED.items()
])
def test_bhu_lug_form(purusha, vacana, expected):
    state = derive("BU", "luG", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू लुँङ् {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_lug_3sg_cli_sic_chain():
    """3.1.43 (cli) and 3.1.44 (cli→sic) must fire for 3sg."""
    state = derive("BU", "luG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.1.43" in applied, "3.1.43 (cli luṅi) must fire for luṅ 3sg"
    assert "3.1.44" in applied, "3.1.44 (cleḥ siḥ) must fire for luṅ 3sg"


def test_bhu_lug_3sg_2477_sic_luk():
    """2.4.77 (sic luk for bhū) must fire for 3sg."""
    state = derive("BU", "luG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "2.4.77" in applied, "2.4.77 (sic luk) must fire for luṅ 3sg"


def test_bhu_lug_3sg_at_augment():
    """6.4.71 (aṭ augment) must fire for 3sg."""
    state = derive("BU", "luG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.4.71" in applied, "6.4.71 (aṭ) must fire for luṅ 3sg"


def test_bhu_lug_3sg_vuk():
    """6.4.88 (vuk for bhū) must fire for 3sg."""
    state = derive("BU", "luG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.4.88" in applied, "6.4.88 (vuk) must fire for luṅ 3sg"


def test_bhu_lug_3sg_6166_v_lopa():
    """6.1.66 (v of vuk drops before t) must fire for 3sg."""
    state = derive("BU", "luG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.1.66" in applied, "6.1.66 (v-lopa before val) must fire for luṅ 3sg"


def test_bhu_lug_no_guna():
    """7.3.84 (guṇa) must NOT fire — vuk intervenes."""
    state = derive("BU", "luG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.84" not in applied, "7.3.84 (guṇa) must NOT fire for luṅ (abhūt not abhavat)"


def test_bhu_lug_3du_3101():
    """3.4.101 (tas→tām) must fire for 3du."""
    state = derive("BU", "luG", "kartari", 3, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (tas→tām) must fire for luṅ 3du"


def test_bhu_lug_3pl_7_1_3():
    """7.1.3 (jh→ant) must fire for 3pl."""
    state = derive("BU", "luG", "kartari", 3, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.1.3" in applied, "7.1.3 (jh→ant) must fire for luṅ 3pl"


def test_bhu_lug_existing_unaffected():
    """All prior lakāra forms must remain correct."""
    from pipelines.tinanta import (
        derive_bhavati, derive_bhavisyati, derive_abhavat,
        derive_bhavet, derive_bhuyat
    )
    assert derive_bhavati().flat_dev()    == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
    assert derive_abhavat().flat_dev()    == "अभवत्"
    assert derive_bhavet().flat_dev()     == "भवेत्"
    assert derive_bhuyat().flat_dev()     == "भूयात्"
