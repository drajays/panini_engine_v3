"""
6.2.157  अच्कावशक्तौ  —  VIDHI

Padaccheda: अच्-कौ अशक्तौ

अच्कावशक्तौ (6.2.157)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_157_ackAvaSakt_157"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_157_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ackAvaSaktO",
    text_dev              = "अच्कावशक्तौ",
    padaccheda_dev        = "अच्-कौ अशक्तौ",
    why_dev               = "(सूत्रम् 6.2.157) अच्कावशक्तौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
