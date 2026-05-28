"""
5.1.21  शताच्च ठन्यतावशते  —  VIDHI

Padaccheda: शतात् च ठन्-यतौ अशते

शताच्च ठन्यतावशते (5.1.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_21_SatAcca_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.21", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SatAcca WanyatAvaSate",
    text_dev              = "शताच्च ठन्यतावशते",
    padaccheda_dev        = "शतात् च ठन्-यतौ अशते",
    why_dev               = "(सूत्रम् 5.1.21) शताच्च ठन्यतावशते।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
