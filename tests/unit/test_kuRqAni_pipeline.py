from __future__ import annotations

import sutras  # noqa: F401

from pipelines.kuRqa_ni_prathama_bahu_napuMsaka import derive_kuRqAni


def test_kuRqAni_surface() -> None:
    s = derive_kuRqAni()
    assert s.flat_slp1() == "kuRqAni"

