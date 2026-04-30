"""
pipelines/pAcakavndArikA_prakriya_37_demo.py — ``prakriya_37`` (**पाचकवृन्दारिका**).

From ``…/separated_prakriyas/prakriya_37_*.json`` — ``ordered_sutra_sequence`` is empty (OCR low
confidence); ``panini_engine_pipeline`` prescribes **१.२.४२**, **६.३.४२**, **६.१.६८** (among others).

Two narrow hooks (glass-box):

  #. ``derive_prakriya_37_karmadhAraya_puMvaw()`` — **1.2.42** · **6.3.42** (registry stamps).
  #. ``derive_prakriya_37_tApanta_sup_lopa()`` — **1.2.41** · **6.1.68** on ``pAcakavndArikA`` + ``s``
     (*ṭāp*-final ``आ`` branch — not the ``hal``-final branch used in ``prakriya_35``/**36**).

Full **२.१.६२**, **१.२.४६**, **२.४.७१**, **४.१.२** … are out of scope for this slice.

CONSTITUTION Art. 7 / 11: ``apply_rule`` only.
"""
from __future__ import annotations

import sutras  # noqa: F401

from engine import apply_rule
from engine.state import State, Term
from phonology import mk
from phonology.varna import parse_slp1_upadesha_sequence


def _mk_pAcikA_vndArikA_witness() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pAcikA")),
        tags={"anga", "prātipadika", "prakriya_37_pAcikA_vndArikA_witness"},
        meta={"upadesha_slp1": "pAcikA"},
    )


def derive_prakriya_37_karmadhAraya_puMvaw() -> State:
    s = State(terms=[_mk_pAcikA_vndArikA_witness()], meta={}, trace=[])

    s.meta["prakriya_37_tatpurusa_upapatti_note"] = True
    s.meta["prakriya_37_1_2_42_arm"] = True
    s = apply_rule("1.2.42", s)

    s.meta["prakriya_37_6_3_42_arm"] = True
    s = apply_rule("6.3.42", s)
    return s


def _mk_pAcakavndArikA_prAtipadika_demo() -> Term:
    return Term(
        kind="prakriti",
        varnas=list(parse_slp1_upadesha_sequence("pAcakavndArikA")),
        tags={"anga", "prātipadika", "prakriya_37_pAcakavndArikA_Atap_demo"},
        meta={"upadesha_slp1": "pAcakavndArikA"},
    )


def _mk_sup_s_pratyaya_after_it_lopa() -> Term:
    return Term(
        kind="pratyaya",
        varnas=[mk("s")],
        tags={"pratyaya", "sup"},
        meta={"upadesha_slp1": "s_sup_aprkta"},
    )


def derive_prakriya_37_tApanta_sup_lopa() -> State:
    s = State(
        terms=[_mk_pAcakavndArikA_prAtipadika_demo(), _mk_sup_s_pratyaya_after_it_lopa()],
        meta={},
        trace=[],
    )
    s = apply_rule("1.2.41", s)
    s.meta["prakriya_37_6_1_68_tApanta_arm"] = True
    s = apply_rule("6.1.68", s)
    return s


__all__ = [
    "derive_prakriya_37_karmadhAraya_puMvaw",
    "derive_prakriya_37_tApanta_sup_lopa",
    "_mk_pAcikA_vndArikA_witness",
    "_mk_pAcakavndArikA_prAtipadika_demo",
    "_mk_sup_s_pratyaya_after_it_lopa",
]
