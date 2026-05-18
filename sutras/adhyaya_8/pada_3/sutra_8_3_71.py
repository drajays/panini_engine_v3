"""
8.3.71  सिवादीनां वाऽड्व्यवायेऽपि  —  VIDHI

Padaccheda: सिव-आदीनाम् वा अट्-अव्यवाये अपि

सिवादीनां वाऽड्व्यवायेऽपि (8.3.71)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_71_sivAdInAM_71"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_71_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sivAdInAM vA'qvyavAye'pi",
    text_dev              = "सिवादीनां वाऽड्व्यवायेऽपि",
    padaccheda_dev        = "सिव-आदीनाम् वा अट्-अव्यवाये अपि",
    why_dev               = "(सूत्रम् 8.3.71) सिवादीनां वाऽड्व्यवायेऽपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
