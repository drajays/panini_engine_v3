"""
5.3.37  आहि च दूरे  —  VIDHI

Padaccheda: आहि (लुप्तप्रथमान्तनिर्देशः) च दूरे

आहि च दूरे (5.3.37)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_3_37_Ahi_37"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_3_37_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Ahi ca dUre",
    text_dev              = "आहि च दूरे",
    padaccheda_dev        = "आहि (लुप्तप्रथमान्तनिर्देशः) च दूरे",
    why_dev               = "(सूत्रम् 5.3.37) आहि च दूरे।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
