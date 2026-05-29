"""Unit tests for ``pipelines/Bavitavyam_split_prakriyas_P002_demo.py`` (**P002**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.Bavitavyam_split_prakriyas_P002_demo import derive_Bavitavyam_split_prakriyas_P002


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P002_spine_order_and_surface():
    """``P002.json`` spine; surface **Bavitavyam** (``6.1.107`` *ati-prakṛti*, not **6.1.101**)."""
    s = derive_Bavitavyam_split_prakriyas_P002()
    ids = _trace_ids(s)
    assert ids.index("3.1.96") < ids.index("1.3.3")
    assert ids.index("1.3.3") < ids.index("1.3.9")
    assert ids.index("1.3.9") < ids.index("7.2.35")
    assert ids.index("7.2.35") < ids.index("7.3.84")
    assert ids.index("7.3.84") < ids.index("6.1.78")
    assert ids.index("6.1.78") < ids.index("1.2.46")
    assert "__MERGE__" in ids
    assert ids.index("1.2.46") < ids.index("__MERGE__")
    mi = ids.index("__MERGE__")
    assert mi < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("7.1.24")
    assert ids.index("7.1.24") < ids.index("6.1.107")

    assert s.samjna_registry.get("1.2.46_krit_pratipadika") is True
    assert s.flat_slp1() == "Bavitavyam"
    assert "6.1.101" not in ids


def test_P002_3_1_96_tavyat_arm_consumed():
    """**3.1.96** clears ``prakriya_P002_3_1_96_tavyat_arm`` after firing."""
    s = derive_Bavitavyam_split_prakriyas_P002()
    assert s.meta.get("prakriya_P002_3_1_96_tavyat_arm") in (None, False)
    assert s.meta.get("prakriya_P002_3_1_96_tavyat_done") is True
