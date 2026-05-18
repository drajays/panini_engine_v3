"""
8.4.14  उपसर्गादसमासेऽपि णोपदेशस्य  —  VIDHI

Padaccheda: उपसर्गात् अ-समासे अपि ण-उपदेशस्य

उपसर्गादसमासेऽपि णोपदेशस्य (8.4.14)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_14_upasargAda_14"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_4_14_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAdasamAse'pi RopadeSasya",
    text_dev              = "उपसर्गादसमासेऽपि णोपदेशस्य",
    padaccheda_dev        = "उपसर्गात् अ-समासे अपि ण-उपदेशस्य",
    why_dev               = "(सूत्रम् 8.4.14) उपसर्गादसमासेऽपि णोपदेशस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
