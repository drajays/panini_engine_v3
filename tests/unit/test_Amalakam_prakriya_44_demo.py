"""Unit tests for ``pipelines/Amalakam_prakriya_44_demo.py`` (``prakriya_44``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.Amalakam_prakriya_44_demo import derive_Amalakam_prakriya_44


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_44_spine_json_vs_machine_index():
    """JSON lists **4.3.132**; *तस्य विकारः* is **4.3.134** on *ashtadhyayi-com*."""
    s = derive_Amalakam_prakriya_44()
    ids = _trace_ids(s)
    assert ids.index("4.1.76") < ids.index("4.3.134")
    assert ids.index("4.3.134") < ids.index("1.2.46")
    assert ids.index("1.2.46") < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("7.1.24")
    assert ids.index("7.1.24") < ids.index("6.1.107")
    assert s.samjna_registry.get("4.3.134_tasya_vikAra_prakriya_44") is True
    assert s.flat_slp1() == "Amalakam"

