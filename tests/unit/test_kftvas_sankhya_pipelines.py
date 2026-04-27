"""*bahukftvaH* / *tAvatkftvaH* / *katikftvaH* — ``pipelines/kftvas_sankhya_avyaya``."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.kftvas_sankhya_avyaya import derive_bahukftvaH, derive_katikftvaH, derive_tAvatkftvaH


def test_derive_bahukftvaH():
    s = derive_bahukftvaH()
    assert s.flat_slp1() == "bahukftvaH"
    assert "5.4.17" in {e.get("sutra_id") for e in s.trace if e.get("status") == "APPLIED"}


def test_derive_tAvatkftvaH():
    s = derive_tAvatkftvaH()
    assert s.flat_slp1() == "tAvatkftvaH"


def test_derive_katikftvaH_includes_6_4_143():
    s = derive_katikftvaH()
    assert s.flat_slp1() == "katikftvaH"
    assert any(
        e.get("sutra_id") == "6.4.143" and e.get("status") == "APPLIED" for e in s.trace
    )
