"""Unit tests for P002-A (vepathuḥ) — canonical krdanta.derive_vepathuH()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_vepathuH


def test_P002_A_render_vepathuH():
    assert derive_vepathuH().flat_slp1() == "vepathuH"


def test_P002_A_spine_core_order():
    s = derive_vepathuH()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.89" in ids
    assert "1.2.46" in ids
    assert "4.1.2" in ids
    assert "8.2.1" in ids
    assert ids.index("3.3.89") < ids.index("1.2.46") < ids.index("4.1.2")
