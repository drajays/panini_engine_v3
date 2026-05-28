"""
6.4.149  सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः  —  VIDHI

Padaccheda: सूर्य-तिष्य-अगस्त्य-मत्स्यानाम् यः उपधायाः

सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः (6.4.149)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_149_sUryatizyA_149"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.149", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.149"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.149",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sUryatizyAgastyamatsyAnAM ya upaDAyAH",
    text_dev              = "सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः",
    padaccheda_dev        = "सूर्य-तिष्य-अगस्त्य-मत्स्यानाम् यः उपधायाः",
    why_dev               = "(सूत्रम् 6.4.149) सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
