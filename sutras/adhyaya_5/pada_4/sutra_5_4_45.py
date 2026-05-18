"""
5.4.45  अपादाने चाहीयरुहोः  —  VIDHI

Padaccheda: अपादाने च अहीयरुहोः

अपादाने चाहीयरुहोः (5.4.45)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_45_apAdAne_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_45_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apAdAne cAhIyaruhoH",
    text_dev              = "अपादाने चाहीयरुहोः",
    padaccheda_dev        = "अपादाने च अहीयरुहोः",
    why_dev               = "(सूत्रम् 5.4.45) अपादाने चाहीयरुहोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
