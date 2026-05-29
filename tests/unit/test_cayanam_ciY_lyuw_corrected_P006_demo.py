"""Unit tests for P006 (cayanam) — canonical krdanta.derive_cayanam() / derive_krt()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.krdanta import derive_cayanam, derive_krt


def test_P006_render_cayanam():
    assert derive_cayanam().flat_slp1() == "cayanam"


def test_P006_pratipadika_cayana():
    s = derive_krt("ciY", krt_upadesha_slp1="lyuw", merge_pratipadika_label="cayana")
    assert s.flat_slp1() == "cayana"


def test_P006_spine_core_order():
    s = derive_cayanam()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert ids.index("3.1.91") < ids.index("3.4.68")
    assert ids.index("3.4.68") < ids.index("3.1.133") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("4.1.2") < ids.index("7.1.24") < ids.index("6.1.107")
