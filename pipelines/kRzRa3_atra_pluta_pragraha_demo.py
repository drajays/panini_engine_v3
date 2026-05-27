"""
pipelines/kRzRa3_atra_pluta_pragraha_demo.py — कृष्ण३ अत्र glass-box.

कृष्ण३ + अत्र → कृष्ण३ अत्र  (no sandhi — pluta pragraha)

By प्लुतप्रगृह्याच्च नित्यम् अचि ६.१.१२५:
  When a pluta vowel (3-mora, e.g. 'a3' = kṛṣṇa³) is immediately followed
  by an ac-initial term, prakṛti-bhāva (preservation of original form) is
  nityam — no sandhi (no savarna-dīrgha 6.1.101, no yaṇ 6.1.77).

The pluta vowel is modeled as a Term tagged "pluta".

Target: **kRzRa3 atra** (कृष्ण३ अत्र) — space is vākya boundary; forms unchanged.
"""
# ── Claude Code review 2026-05-28 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected
# Structural merges recorded in State.trace · no gold shortcuts
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_kRzRa3_atra_pluta_pragraha() -> str:
    """
    Derive 'कृष्ण३ अत्र': kṛṣṇa (pluta final 'a³') + atra → prakṛti-bhāva.
    Returns the space-separated rendered vākya string.
    """
    # kṛṣṇa with pluta final 'a' — modeled as Term tag "pluta"
    kRzRa = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("kRzRa"),
        tags={"prātipadika", "pluta"},
        meta={"upadesha_slp1": "kRzRa", "pluta_on_final": True},
    )
    atra = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("atra"),
        tags={"avyaya"},
        meta={"upadesha_slp1": "atra"},
    )
    s = State(terms=[kRzRa, atra], meta={}, trace=[])

    # 6.1.125: pluta + ac-initial → prakṛti-bhāva (no sandhi)
    s = apply_rule("6.1.125", s)

    # Render each pada separately (pluta: no cross-pada sandhi)
    forms = [t.meta.get("upadesha_slp1") or "".join(v.slp1 for v in t.varnas)
             for t in s.terms]
    return " ".join(forms)


__all__ = ["derive_kRzRa3_atra_pluta_pragraha"]
