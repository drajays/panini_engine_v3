"""Unit tests for ``prakriya_35`` — JSON ``ordered_sutra_sequence`` spine."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.prakriya_35_ordered_demo import (
    derive_prakriya_35_spfSa_ac_karmakartari,
    derive_prakriya_35_vAc_hal_aprkta_sup,
)


def _fired_ids(state) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "APPLIED_VACUOUS", "AUDIT"}:
            out.append(sid)
    return out


def test_vAc_track_flat_and_registry() -> None:
    s = derive_prakriya_35_vAc_hal_aprkta_sup()
    assert s.flat_slp1() == "vAc"
    assert s.samjna_registry.get("6.1.68_vAc_sup_lopa_prakriya_35") is True


def test_vAc_track_spine() -> None:
    s = derive_prakriya_35_vAc_hal_aprkta_sup()
    ids = _fired_ids(s)
    assert ids.index("1.2.41") < ids.index("6.1.68")


def test_spfSa_track_order_1_3_1_then_3_1_62() -> None:
    s = derive_prakriya_35_spfSa_ac_karmakartari()
    ids = _fired_ids(s)
    assert ids.index("1.3.1") < ids.index("3.1.62")
    assert s.samjna_registry.get("1.3.1_prakriya_35_spfSa") is True
    assert s.samjna_registry.get("3.1.62_ac_karmakartari_prakriya_35") is True


def test_spfSa_flat_unchanged() -> None:
    s = derive_prakriya_35_spfSa_ac_karmakartari()
    assert s.flat_slp1() == "spfS"
