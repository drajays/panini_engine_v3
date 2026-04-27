"""
pipelines/mAle_iti_pragRhya_demo.py — *माले इति* (ā-kāra-anta strī *dvivacana* + *iti*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/'माले इति'.md``.

**1.1.11** marks *dvivacana* *anta* in *ī, ū, e, …* as *pragṛhya* (here stem-final *e*
from *ā*+*ī* guṇa). **6.1.78** (*ecoyavāyāvaḥ*) must not split *e* before following *ac*
(*iti*), so the surface stays *māle* + *iti*, not *mālayiti*.

Full *mAlA* → *mAle* in the engine may still use other *sup* paths; this demo fixes the
sandhi boundary in isolation.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def _mAle_iti_state() -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("mAle"),
        tags={"anga", "prātipadika", PRAGHYA_TERM_TAG},
        meta={"upadesha_slp1": "mAlA"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    return State(terms=[left, right], meta={}, trace=[])


def derive_mAle_iti_pragrahya() -> State:
    """*māle* + *iti* — no *e*→*ay* under **6.1.78** at pragṛhya ‖ *ac*."""
    s = _mAle_iti_state()
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.78", s)
    return s


__all__ = ["derive_mAle_iti_pragrahya"]
