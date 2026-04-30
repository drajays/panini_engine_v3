"""Unit tests for ``prakriya_32`` — ``EdaviDa`` + ``jaWilaka`` + ``aDyApaka`` vocatives."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.EdaviDa_jWilaka_aDyApaka_prakriya_32_demo import (
    _mk_aDyApaka,
    _mk_EdaviDa,
    _mk_jaWilaka,
    derive_EdaviDa_triplet_prakriya_32,
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


def test_flat_tape_triplet_concat() -> None:
    s = derive_EdaviDa_triplet_prakriya_32()
    assert s.flat_slp1() == "EdaviDajaWilakaaDyApaka"


def test_prakriya_32_spine_order() -> None:
    s = derive_EdaviDa_triplet_prakriya_32()
    ids = _fired_ids(s)
    spine = [
        "2.3.48",
        "6.1.198",
        "6.1.158",
        "8.1.16",
        "8.1.18",
        "8.1.72",
        "8.1.73",
        "8.1.19",
        "8.1.19",
        "8.2.1",
        "8.4.66",
    ]
    pos = 0
    for sid in spine:
        try:
            pos = ids.index(sid, pos) + 1
        except ValueError as exc:
            raise AssertionError(f"missing {sid} after position {pos}") from exc


def test_registry_and_meta_stamps() -> None:
    s = derive_EdaviDa_triplet_prakriya_32()
    assert s.samjna_registry.get("2.3.48_sAmantrita_triplet_prakriya_32") is True
    assert s.terms[0].meta.get("prakriya_32_EdaviDa_AdyudAtta_note") is True
    assert s.samjna_registry.get("prakriya_32_EdaviDa_svarita_locus") is True
    assert s.terms[1].meta.get("prakriya_32_jWilaka_sarvAnudAtta_note") is True
    assert s.terms[2].meta.get("prakriya_32_aDyApaka_sarvAnudAtta_note") is True
    assert s.samjna_registry.get("prakriya_32_samAnAdhikaraRa") is True


def test_8_1_73_requires_72_registry() -> None:
    s = State(
        terms=[_mk_EdaviDa(), _mk_jaWilaka(), _mk_aDyApaka()],
        meta={"prakriya_32_8_1_73_arm": True},
        trace=[],
    )
    for t in s.terms:
        t.tags.add("sAmantrita")
    s1 = apply_rule("8.1.73", s)
    assert not s1.samjna_registry.get("prakriya_32_samAnAdhikaraRa")


def test_8_1_19_requires_samAnAdhikaraRa() -> None:
    s = State(
        terms=[_mk_EdaviDa(), _mk_jaWilaka(), _mk_aDyApaka()],
        meta={"prakriya_32_8_1_19_jWilaka_arm": True},
        trace=[],
    )
    s.adhikara_stack.append(
        {"id": "8.1.16", "scope_end": "8.3.55", "text_dev": "पदस्य"},
    )
    s.adhikara_stack.append(
        {"id": "8.1.18", "scope_end": "8.1.74", "text_dev": "अनुदात्तं सर्वमपादादौ"},
    )
    for t in s.terms:
        t.tags.add("sAmantrita")
    s1 = apply_rule("8.1.19", s)
    assert not s1.terms[1].meta.get("prakriya_32_jWilaka_sarvAnudAtta_note")
