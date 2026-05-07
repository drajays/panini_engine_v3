"""Unit tests for ``pipelines/vAcA_tRtIyA_strI_corrected_P004_D_demo.py`` (**P004-D**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.vAcA_tRtIyA_strI_corrected_P004_D_demo import (
    derive_vAcA_tRtIyA_strI_corrected_P004_D,
)


def test_P004_D_render_vAcA():
    s = derive_vAcA_tRtIyA_strI_corrected_P004_D()
    assert s.flat_slp1() == "vAcA"


def test_P004_D_spine_has_sup_then_it_lopa():
    s = derive_vAcA_tRtIyA_strI_corrected_P004_D()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "4.1.2" in ids
    assert ids.index("4.1.2") < ids.index("1.3.9")
