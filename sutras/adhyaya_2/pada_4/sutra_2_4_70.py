"""
2.4.70  आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्  —  VIDHI

Padaccheda: आगस्त्य-कौण्डिन्ययोः अगस्ति-कुण्डिनच्

agastya and kaundinyaya as nipatana forms.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_70_agastya_kundini"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["nipatana_kind"]             = "2.4.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AgastyakORqinyayoragastikuRqinac",
    text_dev              = "आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्",
    padaccheda_dev        = "आगस्त्य-कौण्डिन्ययोः अगस्ति-कुण्डिनच्",
    why_dev               = "आगस्त्य-कौण्डिन्ययोः अगस्ति-कुण्डिनच् (२.४.७०)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
