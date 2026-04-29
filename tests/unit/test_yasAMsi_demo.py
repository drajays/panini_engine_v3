from __future__ import annotations

import sutras  # noqa: F401

from pipelines.yasAMsi_jas_shi_num_demo import derive_yasAMsi


def test_yasAMsi_surface() -> None:
    s = derive_yasAMsi()
    assert s.flat_slp1() == "yasAMsi"

