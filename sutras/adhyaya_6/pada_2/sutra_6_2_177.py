"""
6.2.177  उपसर्गात् स्वाङ्गं ध्रुवमपर्शु  —  VIDHI

Padaccheda: उपसर्गात् स्वाङ्गम् ध्रुवम् अपर्शु

उपसर्गात् स्वाङ्गं ध्रुवमपर्शु (6.2.177)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_177_upasargAt_177"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_177_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.177"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.177",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAt svANgaM DruvamaparSu",
    text_dev              = "उपसर्गात् स्वाङ्गं ध्रुवमपर्शु",
    padaccheda_dev        = "उपसर्गात् स्वाङ्गम् ध्रुवम् अपर्शु",
    why_dev               = "(सूत्रम् 6.2.177) उपसर्गात् स्वाङ्गं ध्रुवमपर्शु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
