"""
6.4.153  बिल्वकादिभ्यश्छस्य लुक्  —  VIDHI

Padaccheda: बिल्वक-आदिभ्यः छस्य लुक्

बिल्वकादिभ्यश्छस्य लुक् (6.4.153)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_153_bilvakAdiB_153"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.153", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.153"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.153",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bilvakAdiByaSCasya luk",
    text_dev              = "बिल्वकादिभ्यश्छस्य लुक्",
    padaccheda_dev        = "बिल्वक-आदिभ्यः छस्य लुक्",
    why_dev               = "(सूत्रम् 6.4.153) बिल्वकादिभ्यश्छस्य लुक्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
