"""Unit tests for P004-B (śāṇḍikyaḥ) — canonical taddhita.derive_SANqikyaH()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.taddhita import derive_SANqikyaH


def test_P004_B_render_SANDikyaH():
    assert derive_SANqikyaH().flat_slp1() == "SARqikyaH"


def test_P004_B_spine_core_order():
    s = derive_SANqikyaH()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "4.3.92" in ids
    assert ids.index("4.3.92") < ids.index("2.4.71")
    assert "7.2.117" in ids
    assert "6.4.148" in ids
    assert ids.index("7.2.117") < ids.index("6.4.148")
    assert "8.2.66" in ids
    assert "8.3.15" in ids
