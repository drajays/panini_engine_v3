"""
tests/unit/test_tinanta_bhave_lat.py — भू + लट् + भावे prayoga (9 cells).
"""
from __future__ import annotations

import pytest
from pipelines.tinanta import derive

_BHU_BHAVE_LAT = {
    (3, 1): "भवते",
    (3, 2): "भवेते",
    (3, 3): "भवन्ते",
    (2, 1): "भवसे",
    (2, 2): "भवेथे",
    (2, 3): "भवध्वे",
    (1, 1): "भवे",
    (1, 2): "भवावहे",
    (1, 3): "भवामहे",
}


@pytest.mark.parametrize("purusha,vacana,expected", [
    (pu, va, exp) for (pu, va), exp in _BHU_BHAVE_LAT.items()
])
def test_bhu_bhave_lat(purusha: int, vacana: int, expected: str) -> None:
    state = derive("BU", "laT", "bhave", purusha, vacana)
    assert state.flat_dev() == expected


def test_bhu_bhave_lit_3sg() -> None:
    assert derive("BU", "liT", "bhave", 3, 1).flat_dev() == "बभूवे"
