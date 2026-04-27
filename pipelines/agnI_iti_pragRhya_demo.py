"""
pipelines/agnI_iti_pragRhya_demo.py — *agnī iti* / *vāyū iti* pragṛhya + *iti* sandhi block.

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/अग्नी.md``.

**1.1.11** marks dual *ī/ū/…* *aṅga* as *pragṛhya*; **6.1.125** registers *prakṛti-bhāva*
before *ac*; **6.1.101** / **6.1.77** must not merge *ī+i* or *ū+i* across the boundary.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def _two_word_state(left_slp1: str) -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence(left_slp1),
        tags={"anga", "prātipadika", PRAGHYA_TERM_TAG},
        meta={"upadesha_slp1": left_slp1},
    )
    right = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    return State(terms=[left, right], meta={}, trace=[])


def derive_agnI_iti_pragrahya() -> State:
    """*agnī* + *iti* — no *I+i* dīrgha (6.1.101 blocked at pragṛhya ‖ *ac*)."""
    s = _two_word_state("agnI")
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.101", s)
    return s


def derive_vAyU_iti_no_yan() -> State:
    """*vāyū* + *iti* — armed *iko yaṇ aci* must not turn *U* into *v*."""
    s = _two_word_state("vAyU")
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.77", s)
    return s


__all__ = ["derive_agnI_iti_pragrahya", "derive_vAyU_iti_no_yan"]
