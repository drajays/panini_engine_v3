"""
pipelines/atiri_atinu_kulam_demo.py — अतिरि/अतिनु (neuter adjective) demos.

Source note: `/Users/dr.ajayshukla/Documents/my panini notes/अतिरि कुलम्.md`
Targets (SLP1):
  - atiri  (अतिरि)
  - atinu  (अतिनु)
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _derive_ec_final_neuter_adj(stem_slp1: str) -> State:
    # Treat the compound base (ati+rai / ati+nau) as a ready prātipadika.
    t = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(stem_slp1),
        tags={"prātipadika", "anga", "napuṃsaka"},
        meta={"upadesha_slp1": stem_slp1},
    )
    s = State(terms=[t], meta={"linga": "napuṃsaka"}, trace=[])

    # *एच्* finals: **1.2.47** performs *hrasva* using the same *एच्→इक्* bundle as
    # **1.1.48** (`phonology.ec_ig_hrasva`), without a separate ``apply_rule("1.1.48")``.
    s = apply_rule("1.2.47", s)

    # Attach neuter nom.sg su and drop it via 7.1.23.
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)
    s = apply_rule("7.1.23", s)
    return s


def derive_atiri() -> State:
    # atirE (अतिरै) → atiri
    return _derive_ec_final_neuter_adj("atirE")


def derive_atinu() -> State:
    # atinO (अतिनौ) → atinu
    return _derive_ec_final_neuter_adj("atinO")


__all__ = ["derive_atiri", "derive_atinu"]

