"""
6.1.137  सम्पर्युपेभ्यः करोतौ भूषणे  —  VIDHI

Padaccheda: सम्-परि-उपेभ्यः करोतौ भूषणे

सम्पर्युपेभ्यः करोतौ भूषणे (6.1.137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_137_samparyupe_137"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_1_137_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samparyupeByaH karotO BUzaRe",
    text_dev              = "सम्पर्युपेभ्यः करोतौ भूषणे",
    padaccheda_dev        = "सम्-परि-उपेभ्यः करोतौ भूषणे",
    why_dev               = "(सूत्रम् 6.1.137) सम्पर्युपेभ्यः करोतौ भूषणे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
