"""
4.1.161  मनोर्जातावञ्यतौ षुक् च  —  VIDHI

Padaccheda: मनोः जातौ अञ्-यतौ षुक् च

मनोर्जातावञ्यतौ षुक् च (4.1.161)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_161_manorjAtAv_161"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.161", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.161"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.161",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "manorjAtAvaYyatO zuk ca",
    text_dev              = "मनोर्जातावञ्यतौ षुक् च",
    padaccheda_dev        = "मनोः जातौ अञ्-यतौ षुक् च",
    why_dev               = "(सूत्रम् 4.1.161) मनोर्जातावञ्यतौ षुक् च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
