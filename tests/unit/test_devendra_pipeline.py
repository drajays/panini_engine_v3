from __future__ import annotations

from pipelines.devendra import derive_devendraH, derive_sUryodayaH


def test_devendra_demo():
    s = derive_devendraH()
    assert s.render().endswith("H")


def test_suryodaya_demo():
    s = derive_sUryodayaH()
    assert s.render().endswith("H")

