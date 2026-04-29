from __future__ import annotations

import sutras  # noqa: F401

from pipelines.rAjan_su_rAjA_demo import derive_rAjA


def test_rAjA_surface() -> None:
    s = derive_rAjA()
    assert s.flat_slp1() == "rAjA"

