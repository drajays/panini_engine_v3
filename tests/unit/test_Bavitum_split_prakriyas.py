"""Unit tests for ``pipelines/Bavitum_split_prakriyas_P001_demo.py`` (**P001**)."""

from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY
from pipelines.Bavitum_split_prakriyas_P001_demo import derive_Bavitum_split_prakriyas_P001


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_P001_json_spine_order_and_surface():
    """``P001.json`` spine through **2.4.82**; surface **Bavitum**."""
    s = derive_Bavitum_split_prakriyas_P001()
    ids = _trace_ids(s)
    assert ids.index("3.3.158") < ids.index("1.3.3")
    assert ids.index("1.3.3") < ids.index("1.3.9")
    assert ids.index("1.3.9") < ids.index("7.2.35")
    assert ids.index("7.2.35") < ids.index("7.3.84")
    assert ids.index("7.3.84") < ids.index("6.1.78")
    assert ids.index("6.1.78") < ids.index("1.1.40")
    assert ids.index("1.1.40") < ids.index("4.1.2")
    assert ids.index("4.1.2") < ids.index("2.4.82")

    assert s.samjna_registry.get("3.3.158_samAnakartruka_tumun_prakriya_P001") is True
    assert "avyaya" in s.terms[0].tags
    assert "avyaya" in s.terms[1].tags
    assert s.flat_slp1() == "Bavitum"


def test_P001_registers_narrow_3_3_158():
    r = SUTRA_REGISTRY["3.3.158"]
    assert r.sutra_id == "3.3.158"
    assert "तुमुन्" in r.text_dev
