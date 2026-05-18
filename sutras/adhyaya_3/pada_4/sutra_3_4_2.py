"""
3.4.2  क्रियासमभिहारे लोट्; लोटो हिस्वौ; वा च तध्वमोः  —  VIDHI

Padaccheda: क्रिया-समभिहारे लोट् लोटः हि-स्वौ वा च त-ध्वमोः

krt-suffix rule: क्रियासमभिहारे लोट्; लोटो हिस्वौ; वा च तध्वमोः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_2_kriyAsamaB_2"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_2_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.2"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.2",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kriyAsamaBihAre low; lowo hisvO; vA ca taDvamoH",
    text_dev              = "क्रियासमभिहारे लोट्; लोटो हिस्वौ; वा च तध्वमोः",
    padaccheda_dev        = "क्रिया-समभिहारे लोट् लोटः हि-स्वौ वा च त-ध्वमोः",
    why_dev               = "धातोः प्रत्ययः (३.4.2)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
