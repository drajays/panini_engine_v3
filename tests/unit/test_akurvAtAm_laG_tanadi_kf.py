"""Unit tests for ``pipelines/akurvAtAm_laG_tanadi_kf_P020_demo.py`` (**P020**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.akurvAtAm_laG_tanadi_kf_P020_demo import derive_akurvAtAm_laG_tanadi_kf_P020


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P020_json_spine_order_and_surface():
    s = derive_akurvAtAm_laG_tanadi_kf_P020()
    ids = _trace_ids(s)

    assert ids.index("3.2.111") < ids.index("3.4.78") < ids.index("3.1.79")
    assert ids.index("3.1.79") < ids.index("7.3.84") < ids.index("1.1.51") < ids.index("6.1.77")
    assert ids.index("6.4.110") < ids.index("6.4.71")

    assert s.flat_slp1() == "akurvAtAm"

