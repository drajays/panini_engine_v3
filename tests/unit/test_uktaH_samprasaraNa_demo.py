from __future__ import annotations

import sutras  # noqa: F401

from pipelines.uktaH_samprasaraNa_demo import derive_uktaH


def test_uktaH_surface() -> None:
    s = derive_uktaH()
    assert s.flat_slp1() == "uktaH"

