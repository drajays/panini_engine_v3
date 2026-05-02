"""
pipelines/anekAlSit_sarvasya_paribhasha_P015_demo.py — **P015** paribhāṣā illustration (**1.1.55**).

Source: ``…/my_scripts/final/split_prakriyas_11/P015.json``.

This JSON is an illustration note for **1.1.55** (*anekālśit sarvasya*).
We model two minimal demonstrations:

  1) Apply **1.1.55** as an explicit gate installation (recipe-armed).
  2) Demonstrate a *śit* ādeśa replacing the whole *sthānin* using existing
     **7.1.20** (*jas/śas → śi*) on a neuter aṅga + sup frame.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _anga_neuter_a(stem_slp1: str) -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence(stem_slp1)),
        tags={"anga", "prātipadika", "napuṃsaka"},
        meta={"upadesha_slp1": stem_slp1},
    )


def _sup(up: str) -> Term:
    return Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(up)),
        tags={"pratyaya", "sup", "upadesha"},
        meta={"upadesha_slp1": up},
    )


def derive_anekAlSit_sarvasya_paribhasha_P015_demo() -> State:
    # Start with a minimal witness so 1.1.55 can be applied.
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("a")),
        tags={"anga", "prātipadika", "prakriya_P015_anekalshit_note"},
        meta={"upadesha_slp1": "a"},
    )
    s = State(terms=[t], meta={}, trace=[])

    s.meta["1_1_55_anekal_shit_sarvasya_arm"] = True
    s = apply_rule("1.1.55", s)

    # Demonstration: jas/Sas (whole pratyaya) → Si under 7.1.20.
    s.terms = [_anga_neuter_a("a"), _sup("jas")]
    s = apply_rule("7.1.20", s)
    return s


__all__ = ["derive_anekAlSit_sarvasya_paribhasha_P015_demo"]

