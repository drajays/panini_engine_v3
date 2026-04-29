from __future__ import annotations

import sutras  # noqa: F401

from pipelines.ruNaddhi_rudhadi_snam_demo import derive_ruRadDi


def test_ruRaddhi_surface() -> None:
    s = derive_ruRadDi()
    assert s.flat_slp1() == "ruRadDi"

