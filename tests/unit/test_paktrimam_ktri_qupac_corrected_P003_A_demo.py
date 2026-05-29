"""Unit tests for P003-A (paktrimam) — canonical krdanta.derive_paktrimam()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_paktrimam


def test_P003_A_render_paktrimam():
    s = derive_paktrimam()
    assert s.flat_slp1() == "paktrimam"


def test_P003_A_spine_core_order():
    s = derive_paktrimam()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.88" in ids
    assert "4.4.20" in ids
    assert "8.2.30" in ids
    assert "1.2.46" in ids
    assert "7.1.24" in ids
    assert ids.index("3.3.88") < ids.index("4.4.20") < ids.index("8.2.30")
    assert ids.index("8.2.30") < ids.index("1.2.46") < ids.index("7.1.24")
