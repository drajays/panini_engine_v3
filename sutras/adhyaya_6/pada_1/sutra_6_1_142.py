"""
6.1.142  अपाच्चतुष्पाच्छकुनिष्वालेखने  —  VIDHI

Padaccheda: अपात् चतुष्पात्-शकुनिषु आलेखने

अपाच्चतुष्पाच्छकुनिष्वालेखने (6.1.142)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_142_apAccatuzp_142"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_142_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.142",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apAccatuzpAcCakunizvAleKane",
    text_dev              = "अपाच्चतुष्पाच्छकुनिष्वालेखने",
    padaccheda_dev        = "अपात् चतुष्पात्-शकुनिषु आलेखने",
    why_dev               = "(सूत्रम् 6.1.142) अपाच्चतुष्पाच्छकुनिष्वालेखने।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
