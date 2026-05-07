"""Unit tests for ``pipelines/dhRSTaH_kta_YiDfzf_corrected_P001_B_demo.py`` (**P001-B**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.dhRSTaH_kta_YiDfzf_corrected_P001_B_demo import (
    derive_dhRSTaH_kta_YiDfzf_corrected_P001_B,
)


def test_P001_B_render_dhRSTaH():
    s = derive_dhRSTaH_kta_YiDfzf_corrected_P001_B()
    assert s.render() == "DfzwaH"


def test_P001_B_spine_has_tripadi_and_pratipadika():
    s = derive_dhRSTaH_kta_YiDfzf_corrected_P001_B()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "8.2.1" in ids
    assert "8.4.41" in ids
    assert "1.2.46" in ids
    assert ids.index("8.4.41") < ids.index("1.2.46")
    # Pre-Tripāḍī **8.4.41** so **4.1.2** is not ASIDDHA-blocked after **8.2.1**.
    assert "4.1.2" in ids
    assert ids.index("8.4.41") < ids.index("4.1.2") < ids.index("8.2.1")
