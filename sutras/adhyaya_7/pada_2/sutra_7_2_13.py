"""
7.2.13  कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि  —  VIDHI

Padaccheda: कृ-सृ-भृ-वृ-स्तु-द्रु-स्रु-श्रुवः लिटि

कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि (7.2.13)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_2_13_kfsfBfvfst_13"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_2_13_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.13"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.13",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kfsfBfvfstudrusruSruvo liwi",
    text_dev              = "कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि",
    padaccheda_dev        = "कृ-सृ-भृ-वृ-स्तु-द्रु-स्रु-श्रुवः लिटि",
    why_dev               = "(सूत्रम् 7.2.13) कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
