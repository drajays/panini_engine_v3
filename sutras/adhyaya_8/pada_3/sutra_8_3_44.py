"""
8.3.44  इसुसोः सामर्थ्ये  —  VIDHI

Padaccheda: इसुसोः · सामर्थ्ये

इसुसोः सामर्थ्ये (8.3.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_44_isusoH_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_44_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "isusoH sAmarTye",
    text_dev              = "इसुसोः सामर्थ्ये",
    padaccheda_dev        = "इसुसोः · सामर्थ्ये",
    why_dev               = "(सूत्रम् 8.3.44) इसुसोः सामर्थ्ये।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
