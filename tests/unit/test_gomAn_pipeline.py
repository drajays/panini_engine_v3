"""गोमान् — *go* + *jas* + *matup* + prathamā *su* (note: गोमान्.md)."""

from __future__ import annotations

import sutras  # noqa: F401

from pipelines.gomAn_prathamA_go_matup import derive_gomAn


def test_gomAn_surface_and_spine_order():
    s = derive_gomAn()
    assert s.flat_slp1() == "gomAn"

    tids = [r["sutra_id"] for r in s.trace if r.get("status") in ("APPLIED", "AUDIT")]

    assert "5.2.94" in tids
    assert "1.2.46" in tids
    assert tids.index("1.2.46") < tids.index("2.4.71")
    assert "2.4.71" in tids
    assert "1.4.13" in tids
    assert "7.1.70" in tids
    assert "6.4.14" in tids
    assert "6.1.68" in tids
    assert "8.2.23" in tids

    assert tids.index("7.1.70") < tids.index("6.4.14")
    assert tids.index("6.4.14") < tids.index("6.1.68")
    assert tids.index("6.1.68") < tids.index("8.2.23")
