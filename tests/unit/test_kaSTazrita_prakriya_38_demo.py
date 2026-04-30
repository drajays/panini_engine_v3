"""Unit tests for ``prakriya_38`` — **२.१.३** · **२.१.२३** spine."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.kaSTazrita_prakriya_38_demo import (
    _mk_kaSTazrita_witness,
    derive_kaSTazrita_prakriya_38,
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


def test_flat_tape_unchanged() -> None:
    s = derive_kaSTazrita_prakriya_38()
    assert s.flat_slp1() == "kaSTazrita"


def test_spine_order_and_registry() -> None:
    s = derive_kaSTazrita_prakriya_38()
    ids = _fired_ids(s)
    assert ids.index("2.1.3") < ids.index("2.1.23")
    assert s.samjna_registry.get("2.1.23_dvitIyA_zrita_tatpurusa_prakriya_38") is True


def test_2_1_23_requires_samasa_adhikara() -> None:
    s = State(
        terms=[_mk_kaSTazrita_witness()],
        meta={
            "prakriya_38_dvitIyA_compound_vidhi_note": True,
            "prakriya_38_2_1_23_arm": True,
        },
        trace=[],
    )
    s1 = apply_rule("2.1.23", s)
    assert not s1.samjna_registry.get("2.1.23_dvitIyA_zrita_tatpurusa_prakriya_38")
