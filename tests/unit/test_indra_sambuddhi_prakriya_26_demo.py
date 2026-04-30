"""Unit tests for ``prakriya_26`` — *indra* *sambuddhi* accent (``pipelines/indra_sambuddhi_prakriya_26_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.indra_sambuddhi_prakriya_26_demo import (
    derive_indra_sambuddhi_prakriya_26,
    _mk_indra_sambuddhi,
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


def test_indra_surface_unchanged() -> None:
    s = derive_indra_sambuddhi_prakriya_26()
    assert s.flat_slp1() == "indra"


def test_indra_prakriya_26_spine_order() -> None:
    s = derive_indra_sambuddhi_prakriya_26()
    ids = _fired_ids(s)
    spine = ["2.3.48", "6.1.198", "6.1.158", "8.4.66", "1.2.37"]
    for sid in spine:
        assert sid in ids, f"missing {sid}"
    for i in range(len(spine) - 1):
        assert ids.index(spine[i]) < ids.index(spine[i + 1])


def test_indra_registry_after_demo() -> None:
    s = derive_indra_sambuddhi_prakriya_26()
    assert "sAmantrita" in s.terms[0].tags
    assert s.samjna_registry.get("2.3.48_sAmantrita_indra") is True
    assert s.samjna_registry.get("prakriya_26_svarita_locus") is True
    assert s.meta.get("prakriya_26_subrahmaNyAhvAna_closure") is True
    assert s.terms[0].meta.get("prakriya_26_AdyudAtta_note") is True


def test_6_1_198_requires_sAmantrita() -> None:
    s = State(terms=[_mk_indra_sambuddhi()], meta={"prakriya_26_6_1_198_arm": True}, trace=[])
    s1 = apply_rule("6.1.198", s)
    assert not s1.terms[0].meta.get("prakriya_26_AdyudAtta_note")
