"""Unit tests for ``pipelines/paYcaSazkulam_prakriya_43_demo.py`` (``prakriya_43``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.paYcaSazkulam_prakriya_43_demo import derive_paYcaSazkulam_prakriya_43


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_43_empty_json_spine_commentary():
    """JSON ``ordered_sutra_sequence`` is []; commentary spine uses **5.1.37** then **5.1.28**."""
    s = derive_paYcaSazkulam_prakriya_43()
    ids = _trace_ids(s)
    assert ids.index("4.1.76") < ids.index("5.1.37")
    assert ids.index("5.1.37") < ids.index("5.1.28")
    assert s.samjna_registry.get("5.1.37_tena_krItam_prakriya_43") is True
    assert s.samjna_registry.get("5.1.28_advigu_Tak_luk_prakriya_43") is True
    assert s.flat_slp1() == "paYcaSazkulI"
