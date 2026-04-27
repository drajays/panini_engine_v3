"""
pipelines/amI_atra_pragRhya_demo.py — *अमी अत्र* (*adas* prathamā *bahuvacana* + *atra*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/अमी अत्र.md``.

*Amī* ends in *ī* (**``amI``** SLP1). Before *atra*, **6.1.77** (*iko yaṇ aci*) would give
*ī*+*a* → *y* → *amyatra*. **1.1.11** (*dvivacana* *ī…*) does not name *bahuvacana* here;
**1.1.12** *adaso māt* supplies *pragṛhya* for *ad-*derived *m* + *ī/ū*. **6.1.125**
*prakṛti-bhāva* blocks *yaṇ* — *amī atra*.

The demo stamps ``pragrahya`` on the left *Term* (simulating **1.1.12** prayoga on the
tape). Full *adas*→*amI* *subanta* is not required for the sandhi slice.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def _amI_atra_state() -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("amI"),
        tags={"anga", "prātipadika", PRAGHYA_TERM_TAG},
        meta={"upadesha_slp1": "adas"},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("atra"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "atra"},
    )
    return State(terms=[left, right], meta={}, trace=[])


def derive_amI_atra_pragrahya() -> State:
    """*amī* + *atra* — no *I*→*y* under **6.1.77** at pragṛhya ‖ *ac*."""
    s = _amI_atra_state()
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.77", s)
    return s


__all__ = ["derive_amI_atra_pragrahya"]
