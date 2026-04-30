"""
pipelines/pramANakRtAntarye_paribhasha_P007_demo.py — **P007** paribhāṣā note demo.

Source: ``…/my_scripts/final/split_prakriyas_11/P007.json``.

This JSON is a *paribhāṣā illustration* (no final word derivation).  We model it as:

  1) **1.1.50** (*sthāne ’ntaratamaḥ*) — registers paribhāṣā gates (selection helpers).
  2) **1.1.48** (*ec ig hrasvādeśe*) — demonstrates an explicit niyama that routes
     *ec* shortening to the *ik* domain, independent of “quantity-based antaratama”.

We use a minimal neuter prātipadika ending in **E** (ec-class) so **1.1.48** can
rewrite it to **i** via ``phonology.ec_ig_hrasva``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def derive_pramANakRtAntarye_P007_demo() -> State:
    # Minimal neuter prātipadika with final ec-vowel: E → i under 1.1.48.
    t = Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("E")),
        tags={"prātipadika", "anga", "napuṃsaka"},
        meta={"upadesha_slp1": "E"},
    )
    s = State(terms=[t], meta={"linga": "napuṃsaka"}, trace=[])

    s = apply_rule("1.1.50", s)

    # Arm 1.1.48 explicit wrapper around the ec→ik kernel.
    s.meta["1_1_48_ec_ig_hrasva_arm"] = True
    s.meta["1_1_48_target_term_index"] = 0
    s.meta["1_1_48_target_varna_index"] = 0
    s = apply_rule("1.1.48", s)
    return s


__all__ = ["derive_pramANakRtAntarye_P007_demo"]

