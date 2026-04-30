"""
pipelines/Gic_ca_paribhasha_P012_note_demo.py — **P012** paribhāṣā note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P012.json``.

This JSON is a paribhāṣā illustration note:
  - **1.1.52** *alo ’ntyasya*
  - **1.1.53** *ṅic ca*

No specific derivation is given, so we model it as a minimal gate-installation
demo that applies both paribhāṣās on a non-empty state.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_Gic_ca_paribhasha_P012_note() -> State:
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P012_Gic_ca_note"},
        meta={"upadesha_slp1": "a"},
    )
    s = State(terms=[t], meta={}, trace=[])
    s.meta["prakriya_P012_paribhasha_note_only"] = True
    s = apply_rule("1.1.52", s)
    s = apply_rule("1.1.53", s)
    return s


__all__ = ["derive_Gic_ca_paribhasha_P012_note"]

