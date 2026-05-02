"""
pipelines/sthAnivadAdezO_nalvidhau_paribhasha_P016_note_demo.py — **P016** paribhāṣā note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P016.json``.

This JSON is a paribhāṣā illustration note:
  - **1.1.56** *sthānivadādeśo ’nalvidhau* (gate: substitute behaves like substituend)
  - **1.1.62** *pratyayalope pratyayalakṣaṇam* (gate: pratyaya effects persist after lopa)

No derivation is specified, so this demo only applies both paribhāṣās on a
minimal non-empty ``State``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_sthAnivadAdezO_nalvidhau_paribhasha_P016_note() -> State:
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P016_paribhasha_note"},
        meta={"upadesha_slp1": "a"},
    )
    s = State(terms=[t], meta={}, trace=[])
    s.meta["prakriya_P016_paribhasha_note_only"] = True
    s = apply_rule("1.1.56", s)
    s = apply_rule("1.1.62", s)
    return s


__all__ = ["derive_sthAnivadAdezO_nalvidhau_paribhasha_P016_note"]

