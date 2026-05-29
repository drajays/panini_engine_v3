"""Unit tests for P004-D (vācā) — canonical subanta.derive()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.subanta import derive


def test_P004_D_render_vAcA():
    assert derive("vAc", vibhakti=3, vacana=1, linga="strīliṅga").flat_slp1() == "vAcA"


def test_P004_D_spine_has_sup_then_it_lopa():
    s = derive("vAc", vibhakti=3, vacana=1, linga="strīliṅga")
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "4.1.2" in ids
    assert ids.index("4.1.2") < ids.index("1.3.9")
