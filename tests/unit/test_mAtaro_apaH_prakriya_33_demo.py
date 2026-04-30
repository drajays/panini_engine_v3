"""Unit tests for ``prakriya_33`` — **१.२.४०** / ``mAtaropaH`` accent-demo spine."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.mAtaro_apaH_prakriya_33_demo import (
    _mk_mAtaro_apaH_accent_demo,
    derive_mAtaro_apaH_prakriya_33,
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


def test_flat_tape_demo_word() -> None:
    s = derive_mAtaro_apaH_prakriya_33()
    assert s.flat_slp1() == "mAtaropaH"


def test_spine_has_1_2_40() -> None:
    s = derive_mAtaro_apaH_prakriya_33()
    ids = _fired_ids(s)
    assert "1.2.40" in ids


def test_sannatara_registry() -> None:
    s = derive_mAtaro_apaH_prakriya_33()
    assert s.samjna_registry.get("1.2.40_sannatara_prakriya_33") is True


def test_1_2_40_requires_ekazruti_blocked_note() -> None:
    s = State(
        terms=[_mk_mAtaro_apaH_accent_demo()],
        meta={"prakriya_33_1_2_40_arm": True},
        trace=[],
    )
    s1 = apply_rule("1.2.40", s)
    assert not s1.samjna_registry.get("1.2.40_sannatara_prakriya_33")


def test_1_2_40_requires_demo_tag() -> None:
    t = _mk_mAtaro_apaH_accent_demo()
    t.tags.discard("prakriya_33_mAtaro_apaH_accent_demo")
    s = State(
        terms=[t],
        meta={
            "prakriya_33_1_2_40_arm": True,
            "prakriya_33_ekazruti_na_upapatti_note": True,
        },
        trace=[],
    )
    s1 = apply_rule("1.2.40", s)
    assert not s1.samjna_registry.get("1.2.40_sannatara_prakriya_33")
