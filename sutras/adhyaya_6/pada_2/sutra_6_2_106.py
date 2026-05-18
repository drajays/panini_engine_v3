"""
6.2.106  बहुव्रीहौ विश्वं संज्ञयाम्  —  VIDHI

Padaccheda: बहुव्रीहौ विश्वम् संज्ञायाम्

बहुव्रीहौ विश्वं संज्ञयाम् (6.2.106)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_106_bahuvrIhO_106"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_106_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIhO viSvaM saMjYayAm",
    text_dev              = "बहुव्रीहौ विश्वं संज्ञयाम्",
    padaccheda_dev        = "बहुव्रीहौ विश्वम् संज्ञायाम्",
    why_dev               = "(सूत्रम् 6.2.106) बहुव्रीहौ विश्वं संज्ञयाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
