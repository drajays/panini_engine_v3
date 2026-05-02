"""
pipelines/dyOH_div_subanta_P022_demo.py — P022 (द्यौः)

Goal: derive ``dyOH`` (SLP1) from prātipadika ``div`` in prathamā-ekavacana.

JSON spine (with necessary Tripāḍī gate + it-chain + structural merge):
  - 1.1.50  (context paribhāṣā note)
  - 4.1.2   (attach sup: 1-1 → sU)
  - 1.1.43  (arm: su… is sarvanāmasthāna)
  - 7.1.84  (div → dyOv before sarvanāmasthāna)
  - 8.2.1   (Tripāḍī gate)
  - 8.2.23  (arm: drop final v in dyOv before sU)
  - 1.3.2 → 1.3.9  (it-lopa on sU → s)
  - __MERGE__ (structural: combine into one pada)
  - 8.2.66  (s → ru)
  - 8.3.15  (ru → H)
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_dyOH_div_subanta_P022() -> State:
    div = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("div")),
        tags={"prātipadika", "anga"},
        meta={"upadesha_slp1": "div"},
    )
    s = State(terms=[div], meta={}, trace=[], samjna_registry={})

    s = apply_rule("1.1.50", s)

    # Attach prathamā-ekavacana sU.
    s.meta["vibhakti_vacana"] = "1-1"
    s = apply_rule("4.1.2", s)

    # Mark the sup as sarvanāmasthāna so 7.1.84 can see it.
    s.meta["1_1_43_arm"] = True
    s = apply_rule("1.1.43", s)

    # div → dyOv before sarvanāmasthāna.
    s.meta["P022_7_1_84_div_aut_arm"] = True
    s = apply_rule("7.1.84", s)

    # it-lopa: s~ → s so that 8.2.66 can fire.
    # Must run BEFORE entering Tripāḍī (8.2.1 pūrvatrāsiddham gate).
    s = apply_rule("1.3.2", s)
    s = apply_rule("1.3.9", s)

    # Tripāḍī rules.
    s = apply_rule("8.2.1", s)
    s.meta["P022_8_2_23_final_v_lopa_arm"] = True
    s = apply_rule("8.2.23", s)

    from pipelines.subanta import _pada_merge

    _pada_merge(s)
    s = apply_rule("8.2.66", s)
    s = apply_rule("8.3.15", s)
    return s


__all__ = ["derive_dyOH_div_subanta_P022"]

