"""Unit tests for ``prakriya_25`` — *subrahmaṇyom* (``pipelines/subrahmaRyom_prakriya_25_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.subrahmaRyom_prakriya_25_demo import (
    derive_subrahmaRyom_prakriya_25,
    _mk_subrahmaRyA_om,
)


def _fired_ids(state: State) -> list[str]:
    out: list[str] = []
    for e in state.trace:
        sid = e.get("sutra_id")
        if not sid or not isinstance(sid, str):
            continue
        st = (e.get("status") or "").upper()
        if st in {"APPLIED", "AUDIT"}:
            out.append(sid)
    return out


def test_subrahmaRyom_surface() -> None:
    s = derive_subrahmaRyom_prakriya_25()
    assert s.flat_slp1() == "subrahmaRyom"


def test_subrahmaRyom_ordered_spine() -> None:
    s = derive_subrahmaRyom_prakriya_25()
    ids = _fired_ids(s)
    assert "6.1.152" in ids
    assert "6.1.62" in ids
    assert ids.index("6.1.152") < ids.index("6.1.62")


def test_6_1_62_requires_arm() -> None:
    s = _mk_subrahmaRyA_om()
    s1 = apply_rule("6.1.62", s)
    assert s1.flat_slp1() == "subrahmaRyAom"


def test_6_1_152_requires_arm() -> None:
    s = State(terms=list(_mk_subrahmaRyA_om().terms), meta={}, trace=[])
    s1 = apply_rule("6.1.152", s)
    assert "prakriya_25_6_1_152_arm" not in s1.meta
