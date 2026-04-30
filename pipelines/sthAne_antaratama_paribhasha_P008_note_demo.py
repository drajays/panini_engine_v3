"""
pipelines/sthAne_antaratama_paribhasha_P008_note_demo.py — **P008** paribhāṣā note.

Source: ``…/my_scripts/final/split_prakriyas_11/P008.json``.

The JSON record is an OCR-corrupted continuation note under **1.1.50**
(*sthāne ’ntaratamaḥ*) with no specific derivation reconstructible. We therefore
encode only the paribhāṣā activation as a minimal, rule-based demo:

  **1.1.50** — installs the selection helpers in ``state.paribhasha_gates``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_sthAne_antaratama_paribhasha_P008_note() -> State:
    # Minimal witness so the State is non-empty.
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P008_sthAne_antaratama_note"},
        meta={"upadesha_slp1": "a"},
    )
    s = State(terms=[t], meta={}, trace=[])
    s.meta["prakriya_P008_paribhasha_note_only"] = True
    s = apply_rule("1.1.50", s)
    return s


__all__ = ["derive_sthAne_antaratama_paribhasha_P008_note"]

