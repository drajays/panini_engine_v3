"""Unit tests for ``pipelines/sthAne_antaratama_split_prakriyas_P004_demo.py`` (**P004**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.sthAne_antaratama_split_prakriyas_P004_demo import (
    derive_sthAne_antaratama_split_prakriyas_P004,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P004_trace_order_paribhasha_then_three_dirgha():
    """``P004.json``: **1.1.50** then three **6.1.101** applications."""
    s = derive_sthAne_antaratama_split_prakriyas_P004()
    ids = _trace_ids(s)
    i50 = ids.index("1.1.50")
    sixes = [i for i, sid in enumerate(ids) if sid == "6.1.101"]
    assert len(sixes) == 3
    assert all(i > i50 for i in sixes)
    assert sixes[0] < sixes[1] < sixes[2]


def test_P004_paribhasha_gates_after_1_1_50():
    s = derive_sthAne_antaratama_split_prakriyas_P004()
    assert "sthanantara_vrddhi" in s.paribhasha_gates
    assert "sthanantara_guna" in s.paribhasha_gates


def test_P004_final_surface_and_each_6_1_101_form_after():
    s = derive_sthAne_antaratama_split_prakriyas_P004()
    assert s.flat_slp1() == "maDUdayaH"

    applied_6101 = [x for x in s.trace if x.get("sutra_id") == "6.1.101" and x.get("status") == "APPLIED"]
    assert len(applied_6101) == 3
    assert applied_6101[0].get("form_after") == "daRqAgra"
    assert applied_6101[1].get("form_after") == "daDIdam"
    assert applied_6101[2].get("form_after") == "maDUdayaH"
