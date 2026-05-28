"""
8.2.9  मादुपधायाश्च मतोर्वोऽयवादिभ्यः  —  VIDHI

Padaccheda: मात् उपधायाः च मतोः वः अ-यव-आदिभ्यः

मादुपधायाश्च मतोर्वोऽयवादिभ्यः (8.2.9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_9_mAdupaDAyA_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAdupaDAyASca matorvo'yavAdiByaH",
    text_dev              = "मादुपधायाश्च मतोर्वोऽयवादिभ्यः",
    padaccheda_dev        = "मात् उपधायाः च मतोः वः अ-यव-आदिभ्यः",
    why_dev               = "(सूत्रम् 8.2.9) मादुपधायाश्च मतोर्वोऽयवादिभ्यः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
