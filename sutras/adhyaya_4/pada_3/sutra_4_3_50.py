"""
4.3.50  संवत्सराग्रहायणीभ्यां ठञ् च  —  VIDHI

Padaccheda: संवत्सर-आग्रहायणीभ्याम् ठञ् च

संवत्सराग्रहायणीभ्यां ठञ् च (4.3.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_50_saMvatsarA_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMvatsarAgrahAyaRIByAM WaY ca",
    text_dev              = "संवत्सराग्रहायणीभ्यां ठञ् च",
    padaccheda_dev        = "संवत्सर-आग्रहायणीभ्याम् ठञ् च",
    why_dev               = "(सूत्रम् 4.3.50) संवत्सराग्रहायणीभ्यां ठञ् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
