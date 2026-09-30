"""FINAL_PLAN Track G pins: 6.4.19 प्रक्ष्यति/प्रष्टा; 3.1.45 अशिक्षत्."""
from __future__ import annotations

from pipelines.tinanta import derive


def test_pracch_lrt_lut_drop_tuk() -> None:
    assert derive("06.0149", "lRT", "kartari", 3, 1).flat_slp1() == "prakzyati"
    assert derive("06.0149", "luT", "kartari", 3, 1).flat_slp1() == "prazwA"
    assert derive("06.0149", "laT", "kartari", 3, 1).flat_slp1() == "pfcCati"


def test_sis_ksa_aorist() -> None:
    assert derive("Siza~", "luG", "kartari", 3, 1).flat_slp1() == "aSikzat"
