"""Unit tests for P003-C (uptrimam) — canonical krdanta.derive_uptrimam()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_uptrimam


def test_P003_C_render_uptrimam():
    assert derive_uptrimam().flat_slp1() == "uptrimam"


def test_P003_C_spine_core_order():
    s = derive_uptrimam()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.88" in ids
    assert "4.4.20" in ids
    assert "6.1.15" in ids
    assert "1.1.45" in ids
    assert "6.1.108" in ids
    assert "1.2.46" in ids
    assert "7.1.24" in ids
