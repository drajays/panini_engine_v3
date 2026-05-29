"""Unit tests for P001-A (bhinnaḥ) — canonical krdanta.derive_bhinnaH()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_bhinnaH


def test_P001_A_render_bhinnaH():
    assert derive_bhinnaH().flat_slp1() == "bhinnaH"


def test_P001_A_has_bundle_spine_ids():
    s = derive_bhinnaH()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "8.2.42" in ids
    assert "1.2.46" in ids
    assert ids.index("8.2.42") < ids.index("1.2.46")
