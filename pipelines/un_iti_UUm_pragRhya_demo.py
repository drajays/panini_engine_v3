"""
pipelines/un_iti_UUm_pragRhya_demo.py — *उ + इति* → *ऊँ इति* (Śākalya **1.1.18**, *anārṣa*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/अस्मे इन्द्राबृहस्पती.md``
(*uñ* / *u* before *avaidika* *iti*; **1.1.17** + **1.1.18** with **6.1.125**).

Recipe: ``ANARSHA_META_KEY`` + ``UUM_ADESA_ARM_META`` → **1.1.18** → **6.1.125** → **6.1.77**
/ **6.1.78** — surface stays *ūṃ* + *iti* (no *vaṇ* / *ay*).
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_18 import ANARSHA_META_KEY, UUM_ADESA_ARM_META


def _u_iti_state() -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("u"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "uY"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    return State(terms=[left, right], meta={}, trace=[])


def derive_U_ti_UUm_pragrahya() -> State:
    """*u* + *iti* → *ūṃ* + *iti* (optional Śākalya *ādeśa*), then block sandhi."""
    s = _u_iti_state()
    s.meta[ANARSHA_META_KEY] = True
    s.meta[UUM_ADESA_ARM_META] = True
    s = apply_rule("1.1.18", s)
    s = apply_rule("6.1.125", s)
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.77", s)
    s = apply_rule("6.1.78", s)
    return s


__all__ = ["derive_U_ti_UUm_pragrahya"]
