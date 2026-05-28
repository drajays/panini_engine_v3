"""
6.2.18  पत्यावैश्वर्ये  —  VIDHI

Padaccheda: पत्यौ ऐश्वर्ये

पत्यावैश्वर्ये (6.2.18)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_18_patyAvESva_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "patyAvESvarye",
    text_dev              = "पत्यावैश्वर्ये",
    padaccheda_dev        = "पत्यौ ऐश्वर्ये",
    why_dev               = "(सूत्रम् 6.2.18) पत्यावैश्वर्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
