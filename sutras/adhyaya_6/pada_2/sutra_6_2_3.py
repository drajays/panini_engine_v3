"""
6.2.3  वर्णः वर्णेष्वनेते  —  VIDHI

Padaccheda: वर्णः वर्णेषु अनेते

वर्णः वर्णेष्वनेते (6.2.3)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_3_varRaH_3"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_3_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varRaH varRezvanete",
    text_dev              = "वर्णः वर्णेष्वनेते",
    padaccheda_dev        = "वर्णः वर्णेषु अनेते",
    why_dev               = "(सूत्रम् 6.2.3) वर्णः वर्णेष्वनेते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
