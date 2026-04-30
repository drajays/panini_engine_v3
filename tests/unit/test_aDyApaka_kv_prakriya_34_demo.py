"""Unit tests for ``prakriya_34`` — **अध्यापक क्व** accent spine."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.aDyApaka_kv_prakriya_34_demo import (
    _mk_aDyApaka_kv_vocative,
    _mk_kv_nipAta,
    derive_aDyApaka_kv_prakriya_34,
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


def test_flat_tape_concat() -> None:
    s = derive_aDyApaka_kv_prakriya_34()
    assert s.flat_slp1() == "aDyApakakv"


def test_spine_order() -> None:
    s = derive_aDyApaka_kv_prakriya_34()
    ids = _fired_ids(s)
    spine = [
        "2.3.48",
        "8.1.16",
        "8.1.18",
        "8.1.19",
        "6.1.185",
        "1.2.40",
    ]
    pos = 0
    for sid in spine:
        try:
            pos = ids.index(sid, pos) + 1
        except ValueError as exc:
            raise AssertionError(f"missing {sid} after position {pos}") from exc


def test_meta_and_registry() -> None:
    s = derive_aDyApaka_kv_prakriya_34()
    assert s.samjna_registry.get("2.3.48_sAmantrita_aDyApaka_prakriya_34") is True
    assert s.terms[0].meta.get("prakriya_34_aDyApaka_sarvAnudAtta_note") is True
    assert s.terms[1].meta.get("prakriya_34_kv_svarita_note") is True
    assert s.samjna_registry.get("1.2.40_sannatara_prakriya_34") is True


def test_1_2_40_requires_kv_svarita_note() -> None:
    s = State(
        terms=[_mk_aDyApaka_kv_vocative(), _mk_kv_nipAta()],
        meta={
            "prakriya_34_1_2_40_arm": True,
        },
        trace=[],
    )
    s.terms[0].tags.add("sAmantrita")
    s.terms[0].meta["prakriya_34_aDyApaka_sarvAnudAtta_note"] = True
    s1 = apply_rule("1.2.40", s)
    assert not s1.samjna_registry.get("1.2.40_sannatara_prakriya_34")
