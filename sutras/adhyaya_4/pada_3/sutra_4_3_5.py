"""
4.3.5  परावराधमोत्तमपूर्वाच्च  —  VIDHI

Padaccheda: पर-अवर-अधम-उत्तम-पूर्वात् च

परावराधमोत्तमपूर्वाच्च (4.3.5)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_5_parAvarADa_5"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_5_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.5"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.5",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parAvarADamottamapUrvAcca",
    text_dev              = "परावराधमोत्तमपूर्वाच्च",
    padaccheda_dev        = "पर-अवर-अधम-उत्तम-पूर्वात् च",
    why_dev               = "(सूत्रम् 4.3.5) परावराधमोत्तमपूर्वाच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
