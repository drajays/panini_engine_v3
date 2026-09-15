"""
कथ + णिच् (चुरादिः) — **6.4.48** blocks **7.2.116** via **1.1.57** / परनिमित्तक लोपः.
"""
from __future__ import annotations

from pipelines.kathi_kath_nic_lesson import derive_kathi_kath_nic_lesson


def _applied(s, sid: str) -> bool:
    return any(
        e.get("sutra_id") == sid and e.get("status") == "APPLIED"
        for e in s.trace
    )


def _row(s, sid: str):
    return next((t for t in s.trace if t.get("sutra_id") == sid), None)


def test_kathi_spine_and_no_upadha_vrddhi() -> None:
    s = derive_kathi_kath_nic_lesson()
    assert s.flat_slp1() == "kathi"
    stem = s.terms[0]
    assert "dhatu" in stem.tags
    assert stem.meta.get("upadesha_slp1") == "kathi"

    ids = [t["sutra_id"] for t in s.trace]
    assert ids.index("3.1.26") < ids.index("6.4.48") < ids.index("1.1.57") < ids.index("7.2.116")
    assert _applied(s, "6.4.48")
    assert _applied(s, "3.1.32")

    r116 = _row(s, "7.2.116")
    assert r116 is not None
    assert r116.get("status") in {"SKIPPED", "BLOCKED", "APPLIED_VACUOUS"}
    assert r116.get("form_before") == r116.get("form_after")

    assert stem.meta.get("6_4_48_a_lopa_done") is True
    assert s.paribhasha_gates.get("1.1.57_aca_parasmin_purvavidhau") is True
