"""
pipelines/paYcaSazkulam_prakriya_43_demo.py — ``prakriya_43`` (**पञ्चशष्कुलम्** spine fragment).

Source: ``…/separated_prakriyas/prakriya_43_2026-04-29_14_22_15.json``.

JSON ``ordered_sutra_sequence`` is empty (*scholarly_pass_confidence: low*); the commentary spine used here is the
``panini_engine_pipeline`` block that introduces **तेन क्रीतम्** ``ठक्`` (**5.1.37**) then **अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्**
(**5.1.28**) *luk* on that ``ठक्`` after a *dvigu*.

Earlier समास/*sup*/*ṭak* sandhi steps live elsewhere; witness stem ``paYcaSazkulI`` stands in for **पञ्चशष्कुली**.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _witness_paYcaSazkulam_prakriya_43() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("paYcaSazkulI")),
        tags={"anga", "prātipadika", "prakriya_43_paYcaSazkulam_demo"},
        meta={"upadesha_slp1": "paYcaSazkulI"},
    )


def derive_paYcaSazkulam_prakriya_43() -> State:
    s = State(terms=[_witness_paYcaSazkulam_prakriya_43()], meta={}, trace=[])

    s = apply_rule("4.1.76", s)
    s.meta["prakriya_43_tena_krItam_note"] = True
    s.meta["prakriya_43_5_1_37_arm"] = True
    s = apply_rule("5.1.37", s)

    s.meta["prakriya_43_dvigu_Tak_luk_note"] = True
    s.meta["prakriya_43_5_1_28_arm"] = True
    s = apply_rule("5.1.28", s)
    return s


__all__ = ["derive_paYcaSazkulam_prakriya_43", "_witness_paYcaSazkulam_prakriya_43"]
