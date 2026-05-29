"""Unit tests for ``pipelines/mAtApitarO_dvandva_split_prakriyas_P013_demo.py`` (**P013**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.mAtApitarO_dvandva_split_prakriyas_P013_demo import (
    derive_mAtApitarO_dvandva_split_prakriyas_P013,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P013_trace_order_and_surface():
    s = derive_mAtApitarO_dvandva_split_prakriyas_P013()
    ids = _trace_ids(s)

    assert ids.index("2.1.3") < ids.index("2.2.29") < ids.index("2.2.34")
    assert ids.index("2.2.34") < ids.index("6.3.25") < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("6.1.93")

    assert s.flat_slp1() == "mAtApitarO"

