"""Unit tests for P001-B (dhṛṣṭaḥ) — canonical krdanta.derive_DfzwaH()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_DfzwaH


def test_P001_B_render_dhRSTaH():
    assert derive_DfzwaH().flat_slp1() == "DfzwaH"


def test_P001_B_spine_has_tripadi_and_pratipadika():
    s = derive_DfzwaH()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "8.2.1" in ids
    assert "8.4.41" in ids
    assert "1.2.46" in ids
    assert ids.index("8.4.41") < ids.index("1.2.46")
    assert "4.1.2" in ids
    assert ids.index("8.4.41") < ids.index("4.1.2") < ids.index("8.2.1")
