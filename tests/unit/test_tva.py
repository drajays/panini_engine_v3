"""Unit tests for ``prakriya_23`` — *tvā* (``pipelines/tva_prakriya_23_demo``)."""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State

from pipelines.tva import derive_tva_prakriya_23


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
    assert t0.meta.get("8_1_23_adesha_done") is True
    assert t0.meta.get("sarva_anudAtta_8_1_18") is True


def test_8_1_23_needs_the_adhikaras_and_a_preceding_pada() -> None:
    # Without 8.1.17 / 8.1.18 on the stack the ādeśa has no licence, and a pada-initial tvām is untouched.
    from pipelines.asmad_subanta import _derive
    s = _derive("yuzmad", 2, 1, defer_tripadi=True)
    assert apply_rule("8.1.23", s).flat_slp1() == "tvAm"
    s = apply_rule("8.1.17", apply_rule("8.1.18", s))
    assert apply_rule("8.1.23", s).flat_slp1() == "tvAm"  # no pada before it
