"""Unit tests for ``pipelines/dADikam_taddhita_split_prakriyas_P018_demo.py`` (**P018**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.dADikam_taddhita_split_prakriyas_P018_demo import (
    derive_dADikam_taddhita_split_prakriyas_P018,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P018_json_spine_order_and_surface():
    s = derive_dADikam_taddhita_split_prakriyas_P018()
    ids = _trace_ids(s)

    assert ids.index("4.1.76") < ids.index("4.4.135") < ids.index("7.3.50")
    assert ids.index("7.3.50") < ids.index("7.2.117") < ids.index("6.4.148")
    assert ids.index("6.4.148") < ids.index("4.1.2") < ids.index("7.1.24") < ids.index("6.1.107")

    assert s.flat_slp1() == "dADikam"

