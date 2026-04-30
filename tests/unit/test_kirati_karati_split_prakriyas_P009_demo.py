"""Unit tests for ``pipelines/kirati_karati_split_prakriyas_P009_demo.py`` (**P009**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.kirati_karati_split_prakriyas_P009_demo import (
    derive_kirati_karati_split_prakriyas_P009,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P009_recorded_json_spine_yields_karati():
    """
    P009.json notes classical **kirati**, but the recorded guṇa spine yields **karati**.
    """
    s = derive_kirati_karati_split_prakriyas_P009()
    ids = _trace_ids(s)

    assert ids.index("3.4.78") < ids.index("3.1.77")
    assert ids.index("3.1.77") < ids.index("1.3.8") < ids.index("7.3.84")
    assert ids.index("7.3.84") < ids.index("1.1.51")
    assert ids.index("1.1.51") < ids.index("1.3.3")

    assert s.flat_slp1() == "karati"

