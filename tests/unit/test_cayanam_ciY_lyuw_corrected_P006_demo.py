"""Unit tests for ``pipelines/cayanam_ciY_lyuw_corrected_P006_demo.py`` (**P006**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.cayanam_ciY_lyuw_corrected_P006_demo import (
    derive_cayanam_corrected_P006,
    derive_cayana_pratipadika_corrected_P006,
)


def test_P006_render_cayanam():
    s = derive_cayanam_corrected_P006()
    assert s.flat_slp1() == "cayanam"


def test_P006_pratipadika_cayana():
    s = derive_cayana_pratipadika_corrected_P006()
    assert s.flat_slp1() == "cayana"


def test_P006_spine_core_order():
    s = derive_cayanam_corrected_P006()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.115" in ids
    assert ids.index("3.1.91") < ids.index("3.3.115") < ids.index("3.4.68")
    assert ids.index("3.4.68") < ids.index("3.1.133") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("4.1.2") < ids.index("7.1.24") < ids.index("6.1.107")
