"""Unit tests for ``pipelines/yUpadAru_vfkaBhaya_prakriya_39_demo.py``."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.yUpadAru_vfkaBhaya_prakriya_39_demo import (
    derive_vfkaBhayam_prakriya_39,
    derive_yUpadAru_prakriya_39,
)


def _trace_ids(s):
    """Chronological ``sutra_id`` list (includes ``AUDIT`` adhikāra stamps)."""
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_yUpadAru_surface_and_spine_order():
    s = derive_yUpadAru_prakriya_39()
    assert s.flat_slp1() == "yUpadAru"
    ids = _trace_ids(s)
    assert ids.index("2.1.3") < ids.index("2.1.36")
    assert ids.index("2.1.36") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("2.4.71")
    assert ids.index("2.4.71") < ids.index("1.2.43")
    assert ids.index("1.2.43") < ids.index("2.2.30")
    # second **1.2.46** merge after registry pop
    assert ids.count("1.2.46") == 2
    assert ids.index("2.2.30") < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("7.1.23")
    assert s.meta.get("2_4_71_luk") is True


def test_vfkaBhayam_surface_and_spine_order():
    s = derive_vfkaBhayam_prakriya_39()
    assert s.flat_slp1() == "vfkabhayam"
    ids = _trace_ids(s)
    assert ids.index("2.1.3") < ids.index("2.1.37")
    assert ids.index("2.1.37") < ids.index("2.4.71")
    assert ids.index("2.4.71") < ids.index("7.1.24")
    assert ids.index("7.1.24") < ids.index("6.1.107")
