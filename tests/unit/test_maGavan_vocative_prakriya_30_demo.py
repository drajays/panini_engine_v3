"""Unit tests for ``prakriya_30`` — ``maGavan`` (*maghavan*) vocative."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.maGavan_vocative_prakriya_30_demo import (
    derive_maGavan_vocative_prakriya_30,
    _mk_maGavan_Amant_demo,
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


def test_maGavan_surface() -> None:
    s = derive_maGavan_vocative_prakriya_30()
    assert s.flat_slp1() == "maGavan"


def test_prakriya_30_spine_order() -> None:
    s = derive_maGavan_vocative_prakriya_30()
    ids = _fired_ids(s)
    spine = ["2.3.48", "8.1.16", "8.1.18", "8.1.19"]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    for i in range(len(spine) - 1):
        assert ids.index(spine[i]) < ids.index(spine[i + 1])


def test_sarvAnudAtta_note_and_registry() -> None:
    s = derive_maGavan_vocative_prakriya_30()
    assert s.samjna_registry.get("2.3.48_sAmantrita_maGavan") is True
    assert s.terms[0].meta.get("prakriya_30_sarvAnudAtta_note") is True


def test_8_1_19_requires_8_1_18_adhikAra() -> None:
    s = State(
        terms=[_mk_maGavan_Amant_demo()],
        meta={"prakriya_30_8_1_19_arm": True},
        trace=[],
    )
    s.terms[0].tags.add("sAmantrita")
    s1 = apply_rule("8.1.19", s)
    assert not s1.terms[0].meta.get("prakriya_30_sarvAnudAtta_note")
