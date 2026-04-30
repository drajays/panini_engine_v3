"""Unit tests for ``pipelines/indraRI_prakriya_41_demo.py`` (``prakriya_41``)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.indraRI_prakriya_41_demo import derive_indraRI_prakriya_41


def _trace_ids(s):
    return [x["sutra_id"] for x in s.trace if x.get("sutra_id")]


def test_prakriya_41_spine_opens_strIyadhikAra():
    s = derive_indraRI_prakriya_41()
    assert "4.1.3" in _trace_ids(s)
    assert any(e.get("id") == "4.1.3" for e in s.adhikara_stack)
    assert s.flat_slp1() == "indra"
    assert any("prakriya_41_indrARI_demo" in t.tags for t in s.terms)
