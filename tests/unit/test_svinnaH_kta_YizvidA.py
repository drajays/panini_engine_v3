"""Unit tests for P001-C (svinnaḥ) — canonical krdanta.derive_svinnaH()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_svinnaH


def test_P001_C_render_svinnaH():
    assert derive_svinnaH().flat_slp1() == "svinnaH"


def test_P001_C_spine_bundle_order():
    s = derive_svinnaH()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "6.1.64" in ids
    assert "8.2.42" in ids
    assert "1.2.46" in ids
    assert ids.index("6.1.64") < ids.index("8.2.42") < ids.index("1.2.46")
