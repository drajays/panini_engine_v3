"""
pipelines/AdeH_parasya_paribhasha_note.py — **P014** paribhāṣā note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P014.json``.

This JSON is an illustration note for:
  - **1.1.54** *ādeḥ parasya* (gate: substitution applies to the following element)
and cites **1.3.12** as a common cross-reference in discussion.

No derivation is reconstructible from this JSON alone, so this demo only applies
the relevant paribhāṣā(s) and asserts their gates are installed.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
# ── Claude Code review 2026-05-07 ──────────────────────────────────
# CONSTITUTION-compliant · sūtra-driven · Art.6 firewall respected   
# Structural merges recorded in State.trace · no gold shortcuts      
# ─────────────────────────────────────────────────────────────────────
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_AdeH_parasya_paribhasha_P014_note() -> State:
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P014_AdeH_parasya_note"},
        meta={"upadesha_slp1": "a"},
    )
    s = State(terms=[t], meta={}, trace=[])
    s.meta["prakriya_P014_paribhasha_note_only"] = True

    s = apply_rule("1.1.54", s)

    # Cross-reference cited in JSON; 1.3.12 does not fire here (no dhatu term in this
    # prātipadika context — natural non-application).
    s = apply_rule("1.3.12", s)
    return s


__all__ = ["derive_AdeH_parasya_paribhasha_P014_note"]

