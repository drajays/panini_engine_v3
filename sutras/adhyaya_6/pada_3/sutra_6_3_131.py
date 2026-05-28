"""
6.3.131  मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ  —  VIDHI

Padaccheda: मन्त्रे सोम-अश्व-इन्द्रिय-विश्वदेव्यस्य मतौ

मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ (6.3.131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_131_mantre_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mantre somASvendriyaviSvadevyasya matO",
    text_dev              = "मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ",
    padaccheda_dev        = "मन्त्रे सोम-अश्व-इन्द्रिय-विश्वदेव्यस्य मतौ",
    why_dev               = "(सूत्रम् 6.3.131) मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
