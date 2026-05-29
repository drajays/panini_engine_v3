from __future__ import annotations

import sutras  # noqa: F401

from pipelines.muYcati_tudadi_sa_num_demo import derive_muYcati


def test_muYcati_surface() -> None:
    s = derive_muYcati()
    assert s.flat_slp1() == "muYcati"

