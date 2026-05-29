"""Unit tests for ``pipelines/vaktA_split_prakriyas_P003_demo.py`` (**P003**)."""

from __future__ import annotations

import sutras  # noqa: F401

from engine import SUTRA_REGISTRY
from pipelines.vaktA_split_prakriyas_P003_demo import derive_vaktA_split_prakriyas_P003


def _fired_ids(state):
    out = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "AUDIT"}:
            out.append(sid)
    return out


def test_P003_surface_vaktA():
    s = derive_vaktA_split_prakriyas_P003()
    assert s.flat_slp1() == "vaktA"


def test_P003_kridanta_spine_order():
    s = derive_vaktA_split_prakriyas_P003()
    ids = _fired_ids(s)
    assert ids.index("3.2.135") < ids.index("1.3.3")
    assert ids.index("1.3.3") < ids.index("1.3.9")
    assert ids.index("1.3.9") < ids.index("8.2.1")
    assert ids.index("8.2.1") < ids.index("8.2.30")
    raw_ids = [e.get("sutra_id") for e in s.trace]
    assert "__KRD_MERGE_TRC__" in raw_ids


def test_P003_subanta_trc_order_matches_forward_tests():
    """Align with ``tests/forward/test_forward_krdanta_trc.py::test_trc_subanta_nom_order``."""
    s = derive_vaktA_split_prakriyas_P003()
    ids = [e.get("sutra_id") for e in s.trace if isinstance(e.get("sutra_id"), str)]
    assert ids.index("7.1.94") < ids.index("6.4.11")
    assert ids.index("6.4.11") < ids.index("6.1.66")
    assert ids.index("8.2.1") < ids.index("8.2.7")


def test_P003_registers_3_2_135():
    r = SUTRA_REGISTRY["3.2.135"]
    assert r.sutra_id == "3.2.135"
    assert "तृन्" in r.text_dev
