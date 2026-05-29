"""Unit tests for ``prakriya_36`` — **अर्धभाज्** + *apṛkta* ``स्`` · **6.1.68**."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.ardhaBAj_sup_prakriya_36_demo import (
    _mk_ardhaBAj_prAtipadika_demo,
    _mk_sup_s_pratyaya_after_it_lopa,
    derive_ardhaBAj_sup_prakriya_36,
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


def test_flat_tape_after_hal_lopa() -> None:
    s = derive_ardhaBAj_sup_prakriya_36()
    assert s.flat_slp1() == "ardhaBAj"


def test_spine_1_2_41_then_6_1_68() -> None:
    s = derive_ardhaBAj_sup_prakriya_36()
    ids = _fired_ids(s)
    assert ids.index("1.2.41") < ids.index("6.1.68")


def test_registry_prakriya_36() -> None:
    s = derive_ardhaBAj_sup_prakriya_36()
    assert s.samjna_registry.get("6.1.68_ardhaBAj_sup_lopa_prakriya_36") is True


def test_6_1_68_requires_demo_tag() -> None:
    stem = _mk_ardhaBAj_prAtipadika_demo()
    stem.tags.discard("prakriya_36_ardhaBAj_demo")
    s = State(
        terms=[stem, _mk_sup_s_pratyaya_after_it_lopa()],
        meta={"prakriya_36_ardhaBAj_sup_lopa_arm": True},
        trace=[],
    )
    s = apply_rule("1.2.41", s)
    s1 = apply_rule("6.1.68", s)
    assert not s1.samjna_registry.get("6.1.68_ardhaBAj_sup_lopa_prakriya_36")
