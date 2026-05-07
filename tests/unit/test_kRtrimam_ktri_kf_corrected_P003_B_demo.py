"""Unit tests for ``pipelines/kRtrimam_ktri_kf_corrected_P003_B_demo.py`` (**P003-B**)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.kRtrimam_ktri_kf_corrected_P003_B_demo import (
    derive_kRtrimam_ktri_kf_corrected_P003_B,
)


def test_P003_B_render_kftrimam():
    s = derive_kRtrimam_ktri_kf_corrected_P003_B()
    assert s.flat_slp1() == "kftrimam"


def test_P003_B_spine_core_order():
    s = derive_kRtrimam_ktri_kf_corrected_P003_B()
    ids = [x.get("sutra_id") for x in s.trace if x.get("sutra_id")]
    assert "3.3.88" in ids
    assert "4.4.20" in ids
    assert "7.3.84" in ids
    assert "1.2.46" in ids
    assert "7.1.24" in ids
