from __future__ import annotations

import sutras  # noqa: F401

from pipelines.trApuSam_jAtuSam_taddhita_demo import derive_jAtuSam, derive_trApuSam


def test_trApuSam_surface() -> None:
    s = derive_trApuSam()
    assert s.flat_slp1() == "trApuzam"


def test_jAtuSam_surface() -> None:
    s = derive_jAtuSam()
    assert s.flat_slp1() == "jAtuzam"

