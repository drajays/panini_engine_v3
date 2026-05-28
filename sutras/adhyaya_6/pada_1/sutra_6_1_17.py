"""
6.1.17  लिट्यभ्यासस्योभयेषाम्  —  VIDHI

Padaccheda: लिटि अभ्यासस्य उभयेषाम्

लिट्यभ्यासस्योभयेषाम् (6.1.17)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_17_liwyaByAsa_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liwyaByAsasyoBayezAm",
    text_dev              = "लिट्यभ्यासस्योभयेषाम्",
    padaccheda_dev        = "लिटि अभ्यासस्य उभयेषाम्",
    why_dev               = "(सूत्रम् 6.1.17) लिट्यभ्यासस्योभयेषाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
