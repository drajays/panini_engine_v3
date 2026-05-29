"""Unit tests for P002-B (śvayathuḥ) — canonical krdanta.derive_zvayathuH()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_zvayathuH


def test_P002_B_render_zvayathuH():
    assert derive_zvayathuH().flat_slp1() == "zvayathuH"


def test_P002_B_spine_core_order():
    s = derive_zvayathuH()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.89" in ids
    assert "7.3.84" in ids
    assert "6.1.78" in ids
    assert "1.2.46" in ids
    assert "4.1.2" in ids
    assert "8.2.1" in ids
    assert ids.index("3.3.89") < ids.index("7.3.84") < ids.index("6.1.78")
    assert ids.index("6.1.78") < ids.index("1.2.46") < ids.index("4.1.2")
