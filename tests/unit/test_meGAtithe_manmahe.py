"""Unit tests for ``prakriya_28`` — ``meGAtithe manmahe`` (``pipelines/meGAtithe_manmahe_prakriya_28_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.meGAtithe_manmahe_prakriya_28_demo import (
    derive_meGAtithe_manmahe_prakriya_28,
    _mk_meGAtithe_voc,
    _mk_manmahe_tin,
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


def test_phrase_flat_tape() -> None:
    s = derive_meGAtithe_manmahe_prakriya_28()
    assert s.flat_slp1() == "meGAtithemanmahe"


def test_prakriya_28_spine_order() -> None:
    s = derive_meGAtithe_manmahe_prakriya_28()
    ids = _fired_ids(s)
    spine = ["2.1.2", "6.1.198", "6.1.158", "8.2.1", "8.4.66"]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    for i in range(len(spine) - 1):
        assert ids.index(spine[i]) < ids.index(spine[i + 1])


def test_registry_meta_after_demo() -> None:
    s = derive_meGAtithe_manmahe_prakriya_28()
    assert s.samjna_registry.get("2.1.2_subAmantrite_parA~ggavat_28")
    assert s.terms[0].meta.get("prakriya_28_AdyudAtta_note") is True
    assert s.samjna_registry.get("prakriya_28_svarita_locus") is True


def test_6_1_198_requires_2_1_2_registry() -> None:
    s = State(
        terms=[_mk_meGAtithe_voc(), _mk_manmahe_tin()],
        meta={"prakriya_28_6_1_198_arm": True},
        trace=[],
    )
    s1 = apply_rule("6.1.198", s)
    assert not s1.terms[0].meta.get("prakriya_28_AdyudAtta_note")
