"""
tests/unit/test_tinanta_bhavisyati_lrt.py

Glass-box gold tests for भू + लृट् parasmaipada — all 9 cells.
Verifies the sya-vikarana pipeline (3.1.33 → 3.4.114 → 7.2.35 → 8.3.59).
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive


_BHU_LRT_EXPECTED = {
    (3, 1): "भविष्यति",
    (3, 2): "भविष्यतः",
    (3, 3): "भविष्यन्ति",
    (2, 1): "भविष्यसि",
    (2, 2): "भविष्यथः",
    (2, 3): "भविष्यथ",
    (1, 1): "भविष्यामि",
    (1, 2): "भविष्यावः",
    (1, 3): "भविष्यामः",
}

_PURUSHA_NAME = {3: "प्रथम", 2: "मध्यम", 1: "उत्तम"}
_VACANA_NAME  = {1: "एक", 2: "द्वि", 3: "बहु"}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_LRT_EXPECTED.items()
])
def test_bhu_lrt_form(purusha, vacana, expected):
    state = derive("BU", "lRT", "kartari", purusha, vacana)
    assert state.flat_dev() == expected, (
        f"भू lṛṭ {_PURUSHA_NAME[purusha]}पुरुष {_VACANA_NAME[vacana]}वचन: "
        f"got {state.flat_dev()!r}, expected {expected!r}"
    )


def test_bhu_lrt_trace_has_sya_vikarana():
    """Verify 3.1.33 (sya insertion) appears in the trace for 3sg."""
    state = derive("BU", "lRT", "kartari", 3, 1)
    sutra_ids = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    assert "3.1.33" in sutra_ids, "3.1.33 (sya vikaraṇa) must fire for lṛṭ"
    assert "3.4.114" in sutra_ids, "3.4.114 (sya = ārdhadhātuka) must fire for lṛṭ"
    assert "7.2.35" in sutra_ids, "7.2.35 (iṭ before sya) must fire for lṛṭ"
    assert "8.3.59" in sutra_ids, "8.3.59 (s→ṣ after i) must fire for lṛṭ"


def test_bhu_lrt_diirgha_uttama():
    """Verify 7.3.101 (ato dīrgho yañi) fires for uttama forms (yañ-initial tiṅ)."""
    for pu, va, exp in [(1, 1, "भविष्यामि"), (1, 2, "भविष्यावः"), (1, 3, "भविष्यामः")]:
        state = derive("BU", "lRT", "kartari", pu, va)
        applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
        assert "7.3.101" in applied, (
            f"7.3.101 must fire for uttama {_VACANA_NAME[va]}vacana (form: {exp})"
        )
        assert state.flat_dev() == exp


def test_bhu_lrt_3sg_key_sutras_ordered():
    """Verify the correct sūtra-fire order for 3sg: 3.4.113 before 3.1.33 before 7.2.35."""
    state = derive("BU", "lRT", "kartari", 3, 1)
    applied = [t["sutra_id"] for t in state.trace if t.get("status") == "APPLIED"]
    idx_113 = applied.index("3.4.113")
    idx_133 = applied.index("3.1.33")
    idx_735 = applied.index("7.2.35")
    assert idx_113 < idx_133, "3.4.113 must fire before 3.1.33"
    assert idx_133 < idx_735, "3.1.33 must fire before 7.2.35"
