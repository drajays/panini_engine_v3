"""
2.3.51  ज्ञोऽविदर्थस्य करणे  —  VIDHI

Padaccheda: ज्ञः अ-विद्-अर्थस्य करणे

jna not in knowledge sense takes tritiya for karana.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_51_jna_avida_karane"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_51_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jYo'vidarTasya karaRe",
    text_dev              = "ज्ञोऽविदर्थस्य करणे",
    padaccheda_dev        = "ज्ञः अ-विद्-अर्थस्य करणे",
    why_dev               = "ज्ञः अ-विद्-अर्थस्य करणे (२.३.५१)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
