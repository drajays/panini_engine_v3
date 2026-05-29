"""Unit tests for P004-C (brāhmaṇāḥ) — canonical subanta.derive()."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.subanta import derive


def test_P004_C_render_brAhmaRAH():
    assert derive("brAhmaRa", vibhakti=1, vacana=3, linga="pulliṅga").flat_slp1() == "brAhmaRAH"


def test_P004_C_spine_has_jas_dirgha_visarga():
    s = derive("brAhmaRa", vibhakti=1, vacana=3, linga="pulliṅga")
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "4.1.2" in ids
    assert "6.1.101" in ids
    assert "8.2.66" in ids
    assert "8.3.15" in ids
