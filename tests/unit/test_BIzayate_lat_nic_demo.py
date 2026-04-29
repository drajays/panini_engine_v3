from __future__ import annotations

import sutras  # noqa: F401

from pipelines.BIzayate_lat_nic_demo import derive_BIzayate


def test_BIzayate_surface() -> None:
    s = derive_BIzayate()
    assert s.flat_slp1() == "BIzayate"

