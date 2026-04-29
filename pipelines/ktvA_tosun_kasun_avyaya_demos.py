"""
pipelines/ktvA_tosun_kasun_avyaya_demos.py — demos for **1.1.40** (paribhāṣā).

Targets from user's note `1_1_40.md`:
  - paThitvA   (ktvā)
  - udet oH    (tosun)

These demos focus on the chain:
  1.1.40 (avyaya) → 2.4.82 (sup-luk, ghost) → (optional) tripāḍī ru/visarga.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _anga(slp1: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(slp1)),
        tags={"anga", "prātipadika"},
        meta={"upadesha_slp1": slp1},
    )


def _pratyaya(slp1: str, *, orig: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(slp1)),
        tags={"pratyaya", "krt", "upadesha"},
        meta={"upadesha_slp1": slp1, "upadesha_slp1_original": orig},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def derive_paThitvA() -> State:
    paTh = _anga("paTh")
    # Surface after iṭ etc. is represented directly; ancestry keeps ktvā.
    tvA = _pratyaya("itvA", orig="ktvA")
    s = State(terms=[paTh, tvA], meta={}, trace=[])
    # Add su only to show sup-luk; then 1.1.40+2.4.82 remove it.
    s.terms.append(_sup("s~"))
    s = apply_rule("1.1.40", s)
    s = apply_rule("2.4.82", s)
    return s


def derive_udetoH() -> State:
    ude = _anga("ude")
    tos = _pratyaya("tos", orig="tosun")
    s = State(terms=[ude, tos], meta={}, trace=[])
    s.terms.append(_sup("s~"))
    s = apply_rule("1.1.40", s)
    s = apply_rule("2.4.82", s)
    # Merge to pada and apply ru/visarga on final s of "tos".
    from pipelines.subanta import _pada_merge
    _pada_merge(s)
    s = apply_rule("8.2.1", s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_paThitvA", "derive_udetoH"]

