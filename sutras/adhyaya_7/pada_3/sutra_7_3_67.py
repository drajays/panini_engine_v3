"""
7.3.67  वचोऽशब्दसंज्ञायाम्  —  VIDHI

Padaccheda: वचः अशब्दसंज्ञायाम्

वचोऽशब्दसंज्ञायाम् (7.3.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_67_vacoSabda_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_67_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vaco'SabdasaMjYAyAm",
    text_dev              = "वचोऽशब्दसंज्ञायाम्",
    padaccheda_dev        = "वचः अशब्दसंज्ञायाम्",
    why_dev               = "(सूत्रम् 7.3.67) वचोऽशब्दसंज्ञायाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
