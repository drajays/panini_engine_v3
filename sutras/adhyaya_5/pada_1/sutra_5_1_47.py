"""
5.1.47  तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते  —  VIDHI

Padaccheda: तत् अस्मिन् वृद्धि-आय-लाभ-शुल्क-उपदाः /वाच्य=अर्थ दीयते (क्रियापदम्)

तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते (5.1.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_47_tadasmin_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_47_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadasmin vfdDyAyalABaSulkopadA dIyate",
    text_dev              = "तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते",
    padaccheda_dev        = "तत् अस्मिन् वृद्धि-आय-लाभ-शुल्क-उपदाः /वाच्य=अर्थ दीयते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.1.47) तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
