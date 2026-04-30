"""Unit tests for ``pipelines/paYcagoRiH_dvigu_split_prakriyas_P011_demo.py`` (**P011**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.paYcagoRiH_dvigu_split_prakriyas_P011_demo import (
    derive_paYcagoRiH_dvigu_split_prakriyas_P011,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P011_json_spine_order_and_surface():
    s = derive_paYcagoRiH_dvigu_split_prakriyas_P011()
    ids = _trace_ids(s)

    assert ids.index("2.1.3") < ids.index("2.1.51")
    assert ids.index("2.1.51") < ids.index("8.2.7")
    assert ids.index("8.2.7") < ids.index("4.1.76")
    assert ids.index("4.1.76") < ids.index("5.1.37") < ids.index("5.1.28")
    assert ids.index("5.1.28") < ids.index("2.4.71") < ids.index("1.2.48")
    assert ids.index("1.2.48") < ids.index("4.1.2") < ids.index("8.2.66") < ids.index("8.3.15")

    assert s.flat_slp1() == "paYcagoRiH"

