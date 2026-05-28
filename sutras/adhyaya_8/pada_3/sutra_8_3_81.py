"""
8.3.81  भीरोः स्थानम्  —  VIDHI

Padaccheda: भीरोः स्थानम् (षष्ठ्याः स्थाने प्रथमा)

भीरोः स्थानम् (8.3.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_81_BIroH_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BIroH sTAnam",
    text_dev              = "भीरोः स्थानम्",
    padaccheda_dev        = "भीरोः स्थानम् (षष्ठ्याः स्थाने प्रथमा)",
    why_dev               = "(सूत्रम् 8.3.81) भीरोः स्थानम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
