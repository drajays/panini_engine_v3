"""
4.4.85  अन्नाण्णः  —  VIDHI

Padaccheda: अन्नात् णः

अन्नाण्णः (4.4.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_85_annARRaH_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "annARRaH",
    text_dev              = "अन्नाण्णः",
    padaccheda_dev        = "अन्नात् णः",
    why_dev               = "(सूत्रम् 4.4.85) अन्नाण्णः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
