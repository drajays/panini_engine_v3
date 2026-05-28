"""
2.4.69  उपकादिभ्योऽन्यतरस्यामद्वंद्वे  —  VIDHI

Padaccheda: उपक-आदिभ्यः अन्यतरस्याम् अ-द्वन्द्वे

Optionally for upaka etc. in non-dvandva context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_69_upaka_anyatara"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upakAdiByo'nyatarasyAmadvaMdve",
    text_dev              = "उपकादिभ्योऽन्यतरस्यामद्वंद्वे",
    padaccheda_dev        = "उपक-आदिभ्यः अन्यतरस्याम् अ-द्वन्द्वे",
    why_dev               = "उपक-आदिभ्यः अन्यतरस्याम् अ-द्वन्द्वे (२.४.६९)।",
    anuvritti_from        = ('2.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
