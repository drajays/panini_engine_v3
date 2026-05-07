"""Unit tests for ``pipelines/bhinnaH_kta_Bidi_corrected_P001_A_demo.py`` (bundle **P001-A**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.bhinnaH_kta_Bidi_corrected_P001_A_demo import (
    derive_bhinnaH_kta_Bidi_corrected_P001_A,
)


def test_P001_A_render_bhinnaH():
    s = derive_bhinnaH_kta_Bidi_corrected_P001_A()
    assert s.render() == "bhinnaH"


def test_P001_A_has_bundle_spine_ids():
    s = derive_bhinnaH_kta_Bidi_corrected_P001_A()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "8.2.42" in ids
    assert "1.2.46" in ids
    assert ids.index("8.2.42") < ids.index("1.2.46")
