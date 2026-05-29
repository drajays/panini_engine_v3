from __future__ import annotations

import sutras  # noqa: F401

from pipelines.vande_vad_num_atmanepada_demo import derive_vande


def test_vande_surface() -> None:
    s = derive_vande()
    assert s.flat_slp1() == "vande"

