"""
4.4.107  समानतीर्थे वासी  —  VIDHI

Padaccheda: समानतीर्थे वासी

समानतीर्थे वासी (4.4.107)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_107_samAnatIrT_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_107_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAnatIrTe vAsI",
    text_dev              = "समानतीर्थे वासी",
    padaccheda_dev        = "समानतीर्थे वासी",
    why_dev               = "(सूत्रम् 4.4.107) समानतीर्थे वासी।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
