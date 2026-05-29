"""Unit tests for ``pipelines/adyatanam_taddhita_split_prakriyas_P019_demo.py`` (**P019**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.adyatanam_taddhita_split_prakriyas_P019_demo import (
    derive_adyatanam_taddhita_split_prakriyas_P019,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P019_json_spine_order_and_surface():
    s = derive_adyatanam_taddhita_split_prakriyas_P019()
    ids = _trace_ids(s)

    assert ids.index("4.3.23") < ids.index("1.3.3") < ids.index("1.3.9") < ids.index("7.1.1")
    assert ids.index("7.1.1") < ids.index("4.1.2") < ids.index("7.1.24") < ids.index("6.1.107")

    assert s.flat_slp1() == "adyatanam"

