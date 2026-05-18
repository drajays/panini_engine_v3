"""
5.1.110  विशाखाऽऽषाढादण् मन्थदण्डयोः  —  VIDHI

Padaccheda: विशाखा-आषाढात् अण् मन्थ-दण्डयोः

विशाखाऽऽषाढादण् मन्थदण्डयोः (5.1.110)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_110_viSAKAzA_110"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_110_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viSAKA''zAQAdaR manTadaRqayoH",
    text_dev              = "विशाखाऽऽषाढादण् मन्थदण्डयोः",
    padaccheda_dev        = "विशाखा-आषाढात् अण् मन्थ-दण्डयोः",
    why_dev               = "(सूत्रम् 5.1.110) विशाखाऽऽषाढादण् मन्थदण्डयोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
