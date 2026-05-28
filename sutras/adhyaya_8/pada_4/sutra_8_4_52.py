"""
8.4.52  दीर्घादाचार्याणाम्  —  VIDHI

Padaccheda: दीर्घात् ५/१ आचार्याणाम् ६/३

दीर्घादाचार्याणाम् (8.4.52)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_52_dIrGAdAcAr_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_52_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGAdAcAryARAm",
    text_dev              = "दीर्घादाचार्याणाम्",
    padaccheda_dev        = "दीर्घात् ५/१ आचार्याणाम् ६/३",
    why_dev               = "(सूत्रम् 8.4.52) दीर्घादाचार्याणाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
