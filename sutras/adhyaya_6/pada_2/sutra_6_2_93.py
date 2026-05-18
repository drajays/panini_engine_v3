"""
6.2.93  सर्वं गुणकार्त्स्न्ये  —  VIDHI

Padaccheda: सर्वम् गुण-कार्त्स्न्ये

सर्वं गुणकार्त्स्न्ये (6.2.93)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_93_sarvaM_93"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_93_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.93"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.93",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvaM guRakArtsnye",
    text_dev              = "सर्वं गुणकार्त्स्न्ये",
    padaccheda_dev        = "सर्वम् गुण-कार्त्स्न्ये",
    why_dev               = "(सूत्रम् 6.2.93) सर्वं गुणकार्त्स्न्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
