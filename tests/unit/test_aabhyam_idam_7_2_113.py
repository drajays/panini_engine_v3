from __future__ import annotations

import sutras  # noqa: F401

from pipelines.subanta import derive


def test_idam_trika_dvibhi_aabhyam_flat():
    for vb in (3, 4, 5):
        s = derive("idam", vb, 2)
        assert s.flat_slp1() == "AByAm"


def test_trace_has_hali_lopa_7_2_113_for_idam_trika():
    s = derive("idam", 3, 2)
    ids = [r.get("sutra_id") for r in s.trace]
    assert "7.2.113" in ids
    assert "6.1.97" in ids
    assert "7.3.102" in ids
    assert s.flat_slp1() == "AByAm"


def test_etad_trika_dvibhi_keeps_eta_7_2_113_is_idam_only():
    # 7.2.113 deletes the id of idam only; etad keeps its e-t (एताभ्याम्, not *आभ्याम्*).
    s = derive("etad", 3, 2)
    assert s.flat_slp1() == "etAByAm"


def test_tad_unaffected_by_7_2_113_shape():
    s = derive("tad", 3, 2)
    assert s.flat_slp1() == "tAByAm"
