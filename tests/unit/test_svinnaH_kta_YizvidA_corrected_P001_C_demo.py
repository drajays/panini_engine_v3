"""Unit tests for ``pipelines/svinnaH_kta_YizvidA_corrected_P001_C_demo.py`` (**P001-C**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.svinnaH_kta_YizvidA_corrected_P001_C_demo import (
    derive_svinnaH_kta_YizvidA_corrected_P001_C,
)


def test_P001_C_render_svinnaH():
    s = derive_svinnaH_kta_YizvidA_corrected_P001_C()
    assert s.render() == "svinnaH"


def test_P001_C_spine_bundle_order():
    s = derive_svinnaH_kta_YizvidA_corrected_P001_C()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "6.1.64" in ids
    assert "8.2.42" in ids
    assert "1.2.46" in ids
    assert ids.index("6.1.64") < ids.index("8.2.42") < ids.index("1.2.46")
