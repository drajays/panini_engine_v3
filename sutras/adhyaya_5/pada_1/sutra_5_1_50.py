"""
5.1.50  तद्धरति वहत्यावहति भाराद्वंशादिभ्यः  —  VIDHI

Padaccheda: तद् हरति (क्रियापदम्) वहति (क्रियापदम्) आवहति (क्रियापदम्) भारात् वंश-आदिभ्यः

तद्धरति वहत्यावहति भाराद्वंशादिभ्यः (5.1.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_50_tadDarati_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadDarati vahatyAvahati BArAdvaMSAdiByaH",
    text_dev              = "तद्धरति वहत्यावहति भाराद्वंशादिभ्यः",
    padaccheda_dev        = "तद् हरति (क्रियापदम्) वहति (क्रियापदम्) आवहति (क्रियापदम्) भारात् वंश-आदिभ्यः",
    why_dev               = "(सूत्रम् 5.1.50) तद्धरति वहत्यावहति भाराद्वंशादिभ्यः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
