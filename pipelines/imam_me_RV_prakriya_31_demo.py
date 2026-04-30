"""
pipelines/imam_me_RV_prakriya_31_demo.py — ``prakriya_31`` (**इमं मे** RV accent spine).

From ``…/separated_prakriyas/prakriya_31_*.json`` — corrected ``panini_engine_pipeline``
narrows to **``मे``** after **``इमम्``**: **6.1.197** (*ñaṇityādi* / *prātipadika* first
*udātta* note), **8.1.22** *temayāvekavacasya* (**मे** *anudātta* replacement note),
**8.2.1**, **8.4.66** (*udāttād anudāttasya svaritaḥ*).

JSON ``ordered_sutra_sequence`` lists **8.4.65** (OCR); implementation uses **8.4.66** like
the corrected narrative. Full ``इदम्`` morphophonemics (**7.2.102**, **7.2.109**, **8.2.5**),
*vocative* ``गङ्गे`` …, and **1.2.39** *ekaśruti* are out of scope for this slice.

Flat tape: ``imam`` + ``me`` → ``imamme``.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_imam_acc_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("imam")),
        tags={"anga", "prātipadika", "prakriya_31_idam_acc_demo", "prakriya_31_Riti_pratyaya_demo"},
        meta={"upadesha_slp1": "imam"},
    )


def _mk_me_asmad_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("me")),
        tags={"anga", "prātipadika", "prakriya_31_asmad_me_demo"},
        meta={"upadesha_slp1": "me"},
    )


def derive_imam_me_RV_prakriya_31() -> State:
    s = State(terms=[_mk_imam_acc_demo(), _mk_me_asmad_demo()], meta={}, trace=[])

    s.meta["prakriya_31_6_1_197_arm"] = True
    s = apply_rule("6.1.197", s)

    s.meta["prakriya_31_8_1_22_arm"] = True
    s = apply_rule("8.1.22", s)

    s = apply_rule("8.2.1", s)

    s.meta["prakriya_31_8_4_66_arm"] = True
    s = apply_rule("8.4.66", s)
    return s


__all__ = ["derive_imam_me_RV_prakriya_31", "_mk_imam_acc_demo", "_mk_me_asmad_demo"]
