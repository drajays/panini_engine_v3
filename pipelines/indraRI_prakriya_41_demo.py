"""
pipelines/indraRI_prakriya_41_demo.py — ``prakriya_41`` (**इन्द्राणी** gate).

Source: ``…/separated_prakriyas/prakriya_41_2026-04-29_14_22_01.json``.

JSON ``ordered_sutra_sequence``: **4.1.3** only.

The ``panini_engine_pipeline`` continues with **4.1.49** (*ङीप्* + *आनुक्*), *it*-rules,
**6.1.101**, **8.4.1**/**8.4.2**, etc. — out of scope here; this recipe applies only the
**स्त्रियाम्** (**4.1.3**) *adhikāra* stamp needed before those *strī-pratyaya* blocks.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_indra_prakriya_41() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("indra")),
        tags={"anga", "prātipadika", "prakriya_41_indrARI_demo"},
        meta={"upadesha_slp1": "indra"},
    )


def derive_indraRI_prakriya_41() -> State:
    """Open **4.1.3** *strī*-adhikāra on an **indra** witness (इन्द्राणी spine fragment)."""
    s = State(terms=[_witness_indra_prakriya_41()], meta={}, trace=[])
    s = apply_rule("4.1.3", s)
    return s


__all__ = ["derive_indraRI_prakriya_41", "_witness_indra_prakriya_41"]
