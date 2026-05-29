"""Unit tests for ``prakriya_27`` — *āgaccha* accent (``pipelines/agacCa_phit481_accent_prakriya_27_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.agacCa_phit481_accent_prakriya_27_demo import (
    derive_agacCa_accent_prakriya_27,
    _mk_agacCa_tinanta_accent_demo,
)


def _fired_ids(state: State) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "APPLIED_VACUOUS", "AUDIT"}:
            out.append(sid)
    return out


def test_agacCa_surface_unchanged() -> None:
    s = derive_agacCa_accent_prakriya_27()
    assert s.flat_slp1() == "AgacCa"


def test_agacCa_prakriya_27_spine_order() -> None:
    s = derive_agacCa_accent_prakriya_27()
    ids = _fired_ids(s)
    spine = ["8.1.6", "8.1.28", "8.2.1", "8.4.66"]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    for i in range(len(spine) - 1):
        assert ids.index(spine[i]) < ids.index(spine[i + 1])


def test_agacCa_registry_after_demo() -> None:
    s = derive_agacCa_accent_prakriya_27()
    assert s.samjna_registry.get("prakriya_27_phit481_upasarga_A_udAtta") is True
    assert s.terms[0].meta.get("prakriya_27_gaccha_base_anudAtta_note") is True
    assert s.samjna_registry.get("prakriya_27_svarita_locus") is True


def test_8_1_28_requires_phit481_registry() -> None:
    s = State(
        terms=[_mk_agacCa_tinanta_accent_demo()],
        meta={"prakriya_27_8_1_28_arm": True},
        trace=[],
    )
    s1 = apply_rule("8.1.28", s)
    assert not s1.terms[0].meta.get("prakriya_27_gaccha_base_anudAtta_note")
