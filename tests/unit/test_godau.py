"""Unit tests for ``pipelines/godau_prakriya_46_demo.py`` (``prakriya_46``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.godau_prakriya_46_demo import derive_godau_prakriya_46


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_46_empty_json_spine_commentary_order():
    """JSON ``ordered_sutra_sequence`` is []; commentary spine: **4.1.76** → **4.2.70** → **4.2.82** → **1.2.51**."""
    s = derive_godau_prakriya_46()
    ids = _trace_ids(s)
    assert ids.index("4.1.76") < ids.index("4.2.70")
    assert ids.index("4.2.70") < ids.index("4.2.82")
    assert ids.index("4.2.82") < ids.index("1.2.51")
    assert s.samjna_registry.get("4.2.70_adUrabhava_prakriya_46") is True
    assert s.samjna_registry.get("4.2.82_varaNAdi_luk_prakriya_46") is True
    assert s.samjna_registry.get("1.2.51_lupi_yuktavad_prakriya_46") is True
    assert s.flat_slp1() == "goda"


def test_prakriya_46_machine_index_note():
    """**वरणादिभ्यश्च** is **4.2.82** on ashtadhyayi-com (not **4.2.81** *janapade lup*)."""
    from engine import SUTRA_REGISTRY

    assert "4.2.82" in SUTRA_REGISTRY
    r = SUTRA_REGISTRY["4.2.82"]
    assert r.sutra_id == "4.2.82"
    assert "वरणादिभ्य" in r.text_dev
