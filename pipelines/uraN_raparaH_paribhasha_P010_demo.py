"""
pipelines/uraN_raparaH_paribhasha_P010_demo.py — **P010** paribhāṣā illustration (**1.1.51**).

Source: ``…/my_scripts/final/split_prakriyas_11/P010.json``.

This JSON is an illustration note for **1.1.51** (उरण् रपरः) with two examples:

  1) **kF + guṇa → kar** (a + r) — shown here via **7.3.84** (guṇa) followed by **1.1.51**.
  2) **kF + vṛddhi → kAr** (A + r) — shown here by directly arming **1.1.51** on a tape
     where the vṛddhi substitute **A** is already present, because this repo does not
     yet carry a general “F → A” vṛddhi-vidhi for this context (beyond narrow special cases).

Both slices are executed on the same ``State`` by resetting the tape between them,
so the trace remains a single linear demonstration.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_uraN_raparaH_paribhasha_P010_demo() -> State:
    # Slice 1: kF + guṇa → kar, then 1.1.51 inserts r.
    dhatu = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kF")),
        tags={"dhatu", "anga"},
        meta={"upadesha_slp1": "kF"},
    )
    sap = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence("Sap")),
        tags={"pratyaya", "vikarana", "upadesha", "sarvadhatuka"},
        meta={"upadesha_slp1": "Sap"},
    )
    s = State(terms=[dhatu, sap], meta={}, trace=[])
    s.meta["prakriya_P010_uraN_raparaH_paribhasha_illustration"] = True

    s = apply_rule("7.3.84", s)
    s = apply_rule("1.1.51", s)

    # Slice 2: vṛddhi illustration — A already present as the ādeśa for F.
    dh2 = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("kA")),
        tags={"dhatu", "anga"},
        meta={
            "upadesha_slp1": "kF",
            "urN_rapara_pending": "r",
            # Insert after the ādeśa vowel A (index 1 in "kA").
            "urN_rapara_after_index": 1,
        },
    )
    s.terms = [dh2]
    s = apply_rule("1.1.51", s)
    return s


__all__ = ["derive_uraN_raparaH_paribhasha_P010_demo"]

