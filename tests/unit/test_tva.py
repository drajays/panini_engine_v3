"""Unit tests for ``prakriya_23`` — *tvā* (``pipelines/tva_prakriya_23_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.tva_prakriya_23_demo import derive_tva_prakriya_23, _mk_tvAm_pada


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


def test_tva_prakriya_23_surface() -> None:
    s = derive_tva_prakriya_23()
    assert s.flat_slp1() == "tvA"


def test_tva_prakriya_23_spine_and_anudAtta_meta() -> None:
    s = derive_tva_prakriya_23()
    ids = _fired_ids(s)
    assert "8.1.18" in ids
    assert "8.1.23" in ids
    assert ids.index("8.1.18") < ids.index("8.1.23")
    t0 = s.terms[0]
    assert t0.meta.get("8_1_23_tvA_adesha") is True
    assert t0.meta.get("sarva_anudAtta_8_1_18") is True


def test_8_1_23_skips_without_apAda_adau_arm() -> None:
    s = State(terms=[_mk_tvAm_pada()], meta={}, trace=[])
    s = apply_rule("8.1.18", s)
    s.meta["prakriya_23_8_1_23_arm"] = True
    s1 = apply_rule("8.1.23", s)
    assert s1.flat_slp1() == "tvAm"
    assert not s1.terms[0].meta.get("8_1_23_tvA_adesha")


def test_8_1_23_skips_without_adhikAra_8_1_18_for_anudAtta_flag() -> None:
    s = State(terms=[_mk_tvAm_pada()], meta={}, trace=[])
    s.meta["prakriya_23_apAda_adau_arm"] = True
    s.meta["prakriya_23_8_1_23_arm"] = True
    s1 = apply_rule("8.1.23", s)
    assert s1.flat_slp1() == "tvA"
    assert s1.terms[0].meta.get("8_1_23_tvA_adesha") is True
    assert s1.terms[0].meta.get("sarva_anudAtta_8_1_18") is not True
