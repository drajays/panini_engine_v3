"""
7.1.56  श्रीग्रामण्योश्छन्दसि  —  VIDHI

Padaccheda: श्री-ग्रामण्योः छन्दसि

श्रीग्रामण्योश्छन्दसि (7.1.56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_56_SrIgrAmaRy_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.56", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SrIgrAmaRyoSCandasi",
    text_dev              = "श्रीग्रामण्योश्छन्दसि",
    padaccheda_dev        = "श्री-ग्रामण्योः छन्दसि",
    why_dev               = "(सूत्रम् 7.1.56) श्रीग्रामण्योश्छन्दसि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
