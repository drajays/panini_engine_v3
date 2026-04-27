"""
pipelines/amU_atra_pragRhya_demo.py — *अमू अत्र* (*adas* prathamā *dvivacana* + *atra*).

Source note: ``/Users/dr.ajayshukla/Documents/my panini notes/अमू अत्र’.md``.

After **8.2.80** etc. the dual is *amū* (**``amU``** SLP1). Before *atra*, **6.1.77**
(*iko yaṇ aci*) would map final *ū* before *ac* to *v* (*\\*amvatra*). **1.1.11** / **1.1.12**
scope gives *pragṛhya*; **6.1.125** *prakṛti-bhāva* blocks *yaṇ* — *amū atra*.

Full *adas*→*amU* *subanta* slice is not required here; this isolates the boundary like
``agnI_iti_pragRhya_demo`` / ``pacete_iti_pragRhya_demo``.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine       import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

from sutras.adhyaya_1.pada_1.sutra_1_1_11 import PRAGHYA_TERM_TAG


def _amU_atra_state() -> State:
    left = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("amU"),
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


def derive_amU_atra_pragrahya() -> State:
    """*amū* + *atra* — no *U*→*v* under **6.1.77** at pragṛhya ‖ *ac*."""
    s = _amU_atra_state()
    s.meta["6_1_77_ik_yan_aci_general_arm"] = True
    s = apply_rule("6.1.125", s)
    s = apply_rule("6.1.77", s)
    return s


__all__ = ["derive_amU_atra_pragrahya"]
