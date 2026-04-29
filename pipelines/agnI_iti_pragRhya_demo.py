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

from pipelines.subanta import (
    PADA_MERGE_STEP,
    SUBANTA_RULE_IDS_POST_4_1_2,
    _pada_merge,
    build_initial_state,
    run_subanta_preflight_through_1_4_7,
)
from engine.fixed_point import run_to_fixed_point


def _derive_dual_pada_pre_tripadi(stem_slp1: str) -> State:
    """
    Derive nominative dual (1-2) via the canonical subanta pipeline so **1.1.11**
    assigns pragṛhya from real derivational memory (no manual tagging).
    """
    s = build_initial_state(stem_slp1, 1, 2, "pulliṅga")
    s = run_subanta_preflight_through_1_4_7(s)
    s = apply_rule("4.1.2", s)
    for sid in SUBANTA_RULE_IDS_POST_4_1_2:
        if sid == "8.2.1":  # stop before Tripāḍī gate (vakya-sandhi is pre-tripāḍī)
            break
        if sid == PADA_MERGE_STEP:
            _pada_merge(s)
            continue
        s = apply_rule(sid, s)
    return s


def _append_iti(s: State) -> State:
    """Structural: add the nipāta 'iti' as a second term (vakya boundary demo)."""
    iti = Term(
        kind="prakriti",
        varnas=parse_slp1_upadesha_sequence("iti"),
        tags={"nipāta"},
        meta={"upadesha_slp1": "iti"},
    )
    s.terms.append(iti)
    return s


def derive_agnI_iti_pragrahya() -> State:
    """*agnī* + *iti* — no *I+i* dīrgha (6.1.101 blocked at pragṛhya ‖ *ac*)."""
    s = _derive_dual_pada_pre_tripadi("agni")
    s = _append_iti(s)
    # Vakya-sandhi fixed-point sweep: the engine decides which sūtra fires via cond()
    # and gates (6.1.125 blocks 6.1.77/6.1.101 across pragṛhya ‖ ac).
    s = run_to_fixed_point(["6.1.125", "6.1.77", "6.1.101"], s)
    return s


def derive_vAyU_iti_no_yan() -> State:
    """*vāyū* + *iti* — armed *iko yaṇ aci* must not turn *U* into *v*."""
    s = _derive_dual_pada_pre_tripadi("vAyu")
    s = _append_iti(s)
    s = run_to_fixed_point(["6.1.125", "6.1.77", "6.1.101"], s)
    return s


__all__ = ["derive_agnI_iti_pragrahya", "derive_vAyU_iti_no_yan"]
