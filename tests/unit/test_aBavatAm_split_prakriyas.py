"""Unit tests for ``pipelines/aBavatAm_split_prakriyas_P005_demo.py`` (**P005**)."""

from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY
from pipelines.aBavatAm_split_prakriyas_P005_demo import derive_aBavatAm_split_prakriyas_P005


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P005_json_spine_order_and_surface():
    """``P005.json`` spine; surface **aBavatAm**."""
    s = derive_aBavatAm_split_prakriyas_P005()
    ids = _trace_ids(s)
    assert ids.index("3.2.111") < ids.index("3.1.91")
    assert ids.index("3.1.91") < ids.index("3.4.77")
    assert ids.index("3.4.77") < ids.index("3.4.78")
    assert ids.index("3.4.78") < ids.index("3.4.101")
    assert ids.index("3.4.101") < ids.index("3.1.68")
    assert ids.index("3.1.68") < ids.index("7.3.84")
    assert ids.index("7.3.84") < ids.index("6.1.78")
    assert ids.index("6.1.78") < ids.index("6.4.71")
    assert s.flat_slp1() == "aBavatAm"


def test_P005_registers_new_tin_lakara_sutras():
    for sid in ("3.2.111", "3.4.101"):
        assert SUTRA_REGISTRY[sid].sutra_id == sid
