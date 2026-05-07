"""
4.1.98  गोत्रे कुञ्जादिभ्यश्च्फञ्  —  VIDHI (narrow: corrected-v2 **P004-A**)

Glass-box: after **4.1.92** *apatya* *adhikāra*, append *taddhita* **caPaY** (च्फञ्)
to the frame ``kuYja`` + internal **6-1** *Nas* (*ṣaṣṭhī* proviso).

Recipe arms ``corrected_v2_P004_A_4_1_98_arm`` (CONSTITUTION Art. 7).
"""
from __future__ import annotations

from engine import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State, Term
from phonology.varna import parse_slp1_upadesha_sequence

META_ARM = "corrected_v2_P004_A_4_1_98_arm"
_STEM_UPA = "kuYja"
_TAD_UPA = "caPaY"


def _has_caPaY(state: State) -> bool:
    return any((t.meta.get("upadesha_slp1") or "").strip() == _TAD_UPA for t in state.terms)


def _stem_idx(state: State) -> int | None:
    for i, t in enumerate(state.terms):
        if t.kind != "prakriti":
            continue
        if "anga" not in t.tags:
            continue
        if (t.meta.get("upadesha_slp1") or "").strip() != _STEM_UPA:
            continue
        return i
    return None


def cond(state: State) -> bool:
    if not state.meta.get(META_ARM):
        return False
    if not adhikara_in_effect("4.1.98", state, "4.1.92"):
        return False
    if _stem_idx(state) is None:
        return False
    if _has_caPaY(state):
        return False
    return True


def act(state: State) -> State:
    if not cond(state):
        return state
    pr = Term(
        kind="pratyaya",
        varnas=list(parse_slp1_upadesha_sequence(_TAD_UPA)),
        tags={"pratyaya", "taddhita", "upadesha"},
        meta={"upadesha_slp1": _TAD_UPA},
    )
    state.terms.append(pr)
    state.meta.pop(META_ARM, None)
    return state


SUTRA = SutraRecord(
    sutra_id="4.1.98",
    sutra_type=SutraType.VIDHI,
    text_slp1="gotre kuYjAdibhyaH caPaY",
    text_dev="गोत्रे कुञ्जादिभ्यश्च्फञ्",
    padaccheda_dev="गोत्रे / कुञ्जादिभ्यः / च्फञ्",
    why_dev="कुञ्जादिगणे गोत्रापत्ये च्फञ् — प००४-अ।",
    anuvritti_from=("4.1.92",),
    cond=cond,
    act=act,
)

register_sutra(SUTRA)
