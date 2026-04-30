"""Unit tests for ``pipelines/yuvatiH_stri_split_prakriyas_P006_demo.py`` (**P006**)."""

from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY
from pipelines.yuvatiH_stri_split_prakriyas_P006_demo import (
    derive_yuvatiH_stri_split_prakriyas_P006,
)


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P006_json_spine_order_and_surface():
    s = derive_yuvatiH_stri_split_prakriyas_P006()
    ids = _trace_ids(s)

    assert ids.index("4.1.1") < ids.index("4.1.3")
    assert ids.index("4.1.3") < ids.index("4.1.77")
    assert ids.index("4.1.77") < ids.index("1.3.3")
    assert ids.index("1.3.3") < ids.index("1.3.9")
    assert ids.index("1.3.9") < ids.index("6.4.134")
    assert ids.index("6.4.134") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("8.2.1")
    assert ids.index("8.2.1") < ids.index("8.2.66") < ids.index("8.3.15")

    assert s.flat_slp1() == "yuvatiH"


def test_P006_registers_new_4_1_77():
    r = SUTRA_REGISTRY["4.1.77"]
    assert r.sutra_id == "4.1.77"
    assert "यङश्चाप्" in r.text_dev

