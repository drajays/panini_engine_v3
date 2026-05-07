"""Unit tests for ``pipelines/brAhmaRAH_prathamA_bahu_corrected_P004_C_demo.py`` (**P004-C**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.brAhmaRAH_prathamA_bahu_corrected_P004_C_demo import (
    derive_brAhmaRAH_prathamA_bahu_corrected_P004_C,
)


def test_P004_C_render_brAhmaRAH():
    s = derive_brAhmaRAH_prathamA_bahu_corrected_P004_C()
    assert s.flat_slp1() == "brAhmaRAH"


def test_P004_C_spine_has_jas_dirgha_visarga():
    s = derive_brAhmaRAH_prathamA_bahu_corrected_P004_C()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "4.1.2" in ids
    assert "6.1.101" in ids
    assert "8.2.66" in ids
    assert "8.3.15" in ids
