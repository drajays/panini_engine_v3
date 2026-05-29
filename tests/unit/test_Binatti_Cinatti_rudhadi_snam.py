from __future__ import annotations

import sutras  # noqa: F401

from pipelines.Binatti_Cinatti_rudhadi_snam_demo import derive_Binatti, derive_Cinatti


def test_Binatti_surface() -> None:
    s = derive_Binatti()
    assert s.flat_slp1() == "Binatti"


def test_Cinatti_surface() -> None:
    s = derive_Cinatti()
    assert s.flat_slp1() == "Cinatti"

