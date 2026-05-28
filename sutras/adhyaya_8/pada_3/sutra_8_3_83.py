"""
8.3.83  ज्योतिरायुषः स्तोमः  —  VIDHI

Padaccheda: ज्योतिः-आयुषः स्तोमः

ज्योतिरायुषः स्तोमः (8.3.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_83_jyotirAyuz_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jyotirAyuzaH stomaH",
    text_dev              = "ज्योतिरायुषः स्तोमः",
    padaccheda_dev        = "ज्योतिः-आयुषः स्तोमः",
    why_dev               = "(सूत्रम् 8.3.83) ज्योतिरायुषः स्तोमः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
