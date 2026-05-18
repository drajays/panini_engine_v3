"""
4.4.77  धुरो यड्ढकौ  —  VIDHI

Padaccheda: धुरः यत्-ढकौ

धुरो यड्ढकौ (4.4.77)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_77_Duro_77"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_77_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Duro yaqQakO",
    text_dev              = "धुरो यड्ढकौ",
    padaccheda_dev        = "धुरः यत्-ढकौ",
    why_dev               = "(सूत्रम् 4.4.77) धुरो यड्ढकौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
