"""
tests/unit/test_tinanta_abhavisyat_lrg.py

Glass-box gold tests for भू + लृँङ् (lṛṅ / conditional) parasmaipada — all 9 cells.
Sūtra chain: 3.3.139 → 3.1.33(sya) → 3.4.114(ārdhadhātuka) → 7.2.35(iṭ)
             → 3.4.101/100/7.1.3/3.4.99 → 6.4.71(aṭ) → 7.3.101(dīrgha)
             → 7.3.84(guṇa) → 6.1.78 → 6.1.97 → 8.3.59(ṣatva)
Key: guṇa fires (sya is ārdhadhātuka, not kit); aṭ augment gives 'a' prefix;
     s of sya → ṣ by 8.3.59 (preceded by i of iṭ).
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_LRG_EXPECTED = {
    (3, 1): "अभविष्यत्",
    (3, 2): "अभविष्यताम्",
    (3, 3): "अभविष्यन्",
    (2, 1): "अभविष्यः",
    (2, 2): "अभविष्यतम्",
    (2, 3): "अभविष्यत",
    (1, 1): "अभविष्यम्",
    (1, 2): "अभविष्याव",
    (1, 3): "अभविष्याम",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_LRG_EXPECTED.items()
])
def test_bhu_lrg_form(purusha, vacana, expected):
    state = derive("BU", "lRG", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू लृँङ् {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_lrg_3sg_3339_attachment():
    """3.3.139 (lṛṅ attachment) must fire for 3sg."""
    state = derive("BU", "lRG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.3.139" in applied, "3.3.139 (lṛṅ attachment) must fire"


def test_bhu_lrg_3sg_sya_vikarana():
    """3.1.33 (sya vikaraṇa) must fire for 3sg."""
    state = derive("BU", "lRG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.1.33" in applied, "3.1.33 (sya insertion) must fire"


def test_bhu_lrg_3sg_it_augment():
    """7.2.35 (iṭ augment) must fire for 3sg."""
    state = derive("BU", "lRG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.2.35" in applied, "7.2.35 (iṭ) must fire for lṛṅ 3sg"


def test_bhu_lrg_3sg_at_augment():
    """6.4.71 (aṭ augment) must fire for 3sg."""
    state = derive("BU", "lRG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "6.4.71" in applied, "6.4.71 (aṭ) must fire for lṛṅ 3sg"


def test_bhu_lrg_3sg_guna():
    """7.3.84 (guṇa) MUST fire for lṛṅ — sya is ārdhadhātuka (not kit)."""
    state = derive("BU", "lRG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.84" in applied, "7.3.84 (guṇa) must fire for lṛṅ (abhaviṣyat not abhūṣyat)"


def test_bhu_lrg_3sg_satva():
    """8.3.59 (s→ṣ after IK) must fire for 3sg."""
    state = derive("BU", "lRG", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "8.3.59" in applied, "8.3.59 (ṣatva) must fire for lṛṅ 3sg"


def test_bhu_lrg_3du_3101():
    """3.4.101 (tas→tām) must fire for 3du."""
    state = derive("BU", "lRG", "kartari", 3, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.4.101" in applied, "3.4.101 (tas→tām) must fire for lṛṅ 3du"


def test_bhu_lrg_3pl_7_1_3():
    """7.1.3 (jh→ant) must fire for 3pl."""
    state = derive("BU", "lRG", "kartari", 3, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.1.3" in applied, "7.1.3 (jh→ant) must fire for lṛṅ 3pl"


def test_bhu_lrg_1du_dirgha():
    """7.3.101 (ato dīrgho yañi) must fire for 1du (a→ā before v)."""
    state = derive("BU", "lRG", "kartari", 1, 2)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.101" in applied, "7.3.101 (dīrgha) must fire for lṛṅ 1du"


def test_bhu_lrg_1pl_dirgha():
    """7.3.101 (ato dīrgho yañi) must fire for 1pl (a→ā before m)."""
    state = derive("BU", "lRG", "kartari", 1, 3)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "7.3.101" in applied, "7.3.101 (dīrgha) must fire for lṛṅ 1pl"


def test_bhu_lrg_existing_unaffected():
    """All prior lakāra forms must remain correct."""
    from pipelines.tinanta import (
        derive_bhavati, derive_bhavisyati, derive_abhavat,
        derive_bhavet, derive_bhuyat, derive_abhut
    )
    assert derive_bhavati().flat_dev()    == "भवति"
    assert derive_bhavisyati().flat_dev() == "भविष्यति"
    assert derive_abhavat().flat_dev()    == "अभवत्"
    assert derive_bhavet().flat_dev()     == "भवेत्"
    assert derive_bhuyat().flat_dev()     == "भूयात्"
    assert derive_abhut().flat_dev()      == "अभूत्"
