"""
6.3.116  नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ  —  VIDHI

Padaccheda: नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ

नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ (6.3.116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_116_nahivftivf_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_3_116_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nahivftivfzivyaDirucisahitanizu kvO",
    text_dev              = "नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ",
    padaccheda_dev        = "नहि-वृति-वृषि-व्यधि-रुचि-सहि-तनिषु क्वौ",
    why_dev               = "(सूत्रम् 6.3.116) नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
