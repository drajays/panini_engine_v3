"""Unit tests for ``pipelines/prakftya_lyap_split_prakriyas_P017_demo.py`` (**P017**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.prakftya_lyap_split_prakriyas_P017_demo import (
    derive_prakftya_lyap_split_prakriyas_P017,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P017_json_spine_and_surface():
    s = derive_prakftya_lyap_split_prakriyas_P017()
    ids = _trace_ids(s)

    assert ids.index("3.4.21") < ids.index("7.1.37")
    assert ids.index("7.1.37") < ids.index("1.3.8") < ids.index("1.3.9")
    assert ids.index("1.3.9") < ids.index("6.1.71") < ids.index("1.1.40")
    assert ids.index("1.1.40") < ids.index("4.1.2") < ids.index("2.4.82")

    assert s.flat_slp1() == "prakftya"

