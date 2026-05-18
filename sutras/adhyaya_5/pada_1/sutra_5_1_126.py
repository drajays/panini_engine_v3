"""
5.1.126  सख्युर्यः  —  VIDHI

Padaccheda: सख्युः यः

सख्युर्यः (5.1.126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_126_saKyuryaH_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_126_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saKyuryaH",
    text_dev              = "सख्युर्यः",
    padaccheda_dev        = "सख्युः यः",
    why_dev               = "(सूत्रम् 5.1.126) सख्युर्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
