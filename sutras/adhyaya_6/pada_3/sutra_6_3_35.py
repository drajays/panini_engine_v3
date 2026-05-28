"""
6.3.35  तसिलादिषु आकृत्वसुचः  —  VIDHI

Padaccheda: तसिलादिषु आ कृत्वसुचः

तसिलादिषु आकृत्वसुचः (6.3.35)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_35_tasilAdizu_35"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.35",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tasilAdizu AkftvasucaH",
    text_dev              = "तसिलादिषु आकृत्वसुचः",
    padaccheda_dev        = "तसिलादिषु आ कृत्वसुचः",
    why_dev               = "(सूत्रम् 6.3.35) तसिलादिषु आकृत्वसुचः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
