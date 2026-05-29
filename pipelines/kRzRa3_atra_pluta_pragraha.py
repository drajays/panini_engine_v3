"""
pipelines/kRzRa3_atra_pluta_pragraha.py — कृष्ण३ अत्र glass-box.

कृष्ण३ + अत्र  →  कृष्ण३ अत्र   (prakṛti-bhāva — no sandhi)

Rule chain:
  6.1.125 प्लुतप्रगृह्याच्च नित्यम् अचि:
    "pluta" tag on left Term + ac-initial right Term → prakṛti-bhāva (nityam).
    Stamps right.meta[_META_ACK] so 6.1.101 savarna-dīrgha is suppressed.

Contrast: kṛṣṇa (non-pluta) + atra → 6.1.101 would fuse a+a → ā → "kṛṣṇātra".
With pluta: kṛṣṇa³ + atra → forms preserved unchanged → "kṛṣṇa3 atra".

SLP1 note: pluta (3-mora) rendered as trailing "3" in the vākya string
(traditional IAST: kṛṣṇa3 for कृष्ण३).

Target: **kRzRa3 atra** (कृष्ण३ अत्र)
"""
# ── Claude Code review 2026-05-28 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected
# Structural merges recorded in State.trace · no gold shortcuts
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from engine.trace import TRACE_STATUSES_FIRED
from phonology.varna import parse_slp1_upadesha_sequence


def _render_pluta_vakya(s: State) -> str:
    """Render vākya with trailing '3' on any Term tagged 'pluta'."""
    parts = []
    for t in s.terms:
        slp1 = "".join(v.slp1 for v in t.varnas)
        if "pluta" in t.tags:
            slp1 += "3"
        parts.append(slp1)
    return " ".join(parts)


def derive_kRzRa3_atra_pluta_pragraha() -> State:
    """
    kṛṣṇa (pluta final 'a³') + atra → prakṛti-bhāva by 6.1.125.
    Returns State; call _render_pluta_vakya(s) for "kRzRa3 atra".
    """
    kRzRa = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("kRzRa"),
        tags={"prātipadika", "pluta"},
        meta={"upadesha_slp1": "kRzRa", "pluta_on_final": "a"},
    )
    atra = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("atra"),
        tags={"avyaya"},
        meta={"upadesha_slp1": "atra"},
    )
    s = State(terms=[kRzRa, atra], meta={}, trace=[])

    # 6.1.125 प्लुतप्रगृह्याच्च नित्यम् अचि:
    # pluta + ac-initial → stamp _META_ACK on atra, record in samjna_registry
    s = apply_rule("6.1.125", s)
    return s


def render_kRzRa3_atra(s: State | None = None) -> str:
    """Return 'kRzRa3 atra' from a derived State (or derive fresh)."""
    if s is None:
        s = derive_kRzRa3_atra_pluta_pragraha()
    return _render_pluta_vakya(s)


__all__ = [
    "derive_kRzRa3_atra_pluta_pragraha",
    "render_kRzRa3_atra",
    "_render_pluta_vakya",
]
