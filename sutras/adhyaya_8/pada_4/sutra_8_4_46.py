"""
8.4.46  अचो रहाभ्यां द्वे  —  VIDHI

Padaccheda: अचः र-हाभ्याम् द्वे

अचो रहाभ्यां द्वे (8.4.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_46_aco_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aco rahAByAM dve",
    text_dev              = "अचो रहाभ्यां द्वे",
    padaccheda_dev        = "अचः र-हाभ्याम् द्वे",
    why_dev               = "(सूत्रम् 8.4.46) अचो रहाभ्यां द्वे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
