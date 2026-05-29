"""Unit tests for ``prakriya_37`` — **पाचकवृन्दारिका** spine (narrow slices)."""
from __future__ import annotations

import sutras  # noqa: F401

from pipelines.pAcakavndArikA_prakriya_37_demo import (
    derive_prakriya_37_karmadhAraya_puMvaw,
    derive_prakriya_37_tApanta_sup_lopa,
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


def test_karmadhAraya_spine() -> None:
    s = derive_prakriya_37_karmadhAraya_puMvaw()
    ids = _fired_ids(s)
    assert ids.index("1.2.42") < ids.index("6.3.42")
    assert s.samjna_registry.get("1.2.42_karmadhAraya_prakriya_37") is True
    assert s.samjna_registry.get("6.3.42_puMvaw_prakriya_37") is True


def test_tApanta_sup_lopa_flat_and_registry() -> None:
    s = derive_prakriya_37_tApanta_sup_lopa()
    assert s.flat_slp1() == "pAcakavndArikA"
    assert s.samjna_registry.get("6.1.68_tApanta_sup_lopa_prakriya_37") is True


def test_tApanta_spine_order() -> None:
    s = derive_prakriya_37_tApanta_sup_lopa()
    ids = _fired_ids(s)
    assert ids.index("1.2.41") < ids.index("6.1.68")
