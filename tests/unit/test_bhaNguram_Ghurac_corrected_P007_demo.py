"""Unit tests for P007 (bhaṅguram) — canonical krdanta.derive_bhaNguram()."""

from __future__ import annotations

from pipelines.krdanta import derive_bhaNguram


def test_P007_full_pada_bhaNguram():
    assert derive_bhaNguram().flat_slp1() == "BaNguram"


def test_P007_spine_core_ids():
    s = derive_bhaNguram()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.2.161" in ids
    assert "1.2.46" in ids
    assert "8.2.66" in ids
