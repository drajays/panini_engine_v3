"""Unit tests for ``prakriya_29`` — ``gaurAvaskandin`` (``pipelines/gaurAvaskandin_prakriya_29_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.gaurAvaskandin_prakriya_29_demo import (
    derive_gaurAvaskandin_prakriya_29,
    _mk_gaurAvaskandin_vocative_demo,
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


def test_gaurAvaskandin_surface() -> None:
    s = derive_gaurAvaskandin_prakriya_29()
    assert s.flat_slp1() == "gaurAvaskandin"


def test_prakriya_29_spine_order() -> None:
    s = derive_gaurAvaskandin_prakriya_29()
    ids = _fired_ids(s)
    spine = ["2.3.48", "6.1.197", "6.1.158", "6.1.198", "8.2.1", "8.4.66"]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    for i in range(len(spine) - 1):
        assert ids.index(spine[i]) < ids.index(spine[i + 1])


def test_registry_meta_after_demo() -> None:
    s = derive_gaurAvaskandin_prakriya_29()
    assert s.samjna_registry.get("2.3.48_sAmantrita_gaurAvaskandin") is True
    assert s.terms[0].meta.get("prakriya_29_YiRityAdi_first_udAtta_note") is True
    assert s.terms[0].meta.get("prakriya_29_AdyudAtta_note") is True
    assert s.samjna_registry.get("prakriya_29_svarita_locus") is True


def test_6_1_197_requires_sAmantrita() -> None:
    s = State(
        terms=[_mk_gaurAvaskandin_vocative_demo()],
        meta={"prakriya_29_6_1_197_arm": True},
        trace=[],
    )
    s1 = apply_rule("6.1.197", s)
    assert not s1.terms[0].meta.get("prakriya_29_YiRityAdi_first_udAtta_note")
