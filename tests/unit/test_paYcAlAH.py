"""Unit tests for ``pipelines/paYcAlAH.py`` (``prakriya_45``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.paYcAlAH import derive_paYcAlAH_prakriya_45


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_45_empty_json_spine_commentary():
    """JSON ``ordered_sutra_sequence`` is []; commentary spine highlights **1.2.51**."""
    s = derive_paYcAlAH_prakriya_45()
    assert "1.2.51" in _trace_ids(s)
    assert s.samjna_registry.get("1.2.51_lupi_yuktavad_prakriya_45") is True
    assert s.flat_slp1() == "paYcAla"
