"""
2.3.38  षष्ठी चानादरे  —  VIDHI

Padaccheda: षष्ठी च अनादरे

Sasthi also in contempt/disregard context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_38_sasthi_anadare"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_38_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zazWI cAnAdare",
    text_dev              = "षष्ठी चानादरे",
    padaccheda_dev        = "षष्ठी च अनादरे",
    why_dev               = "षष्ठी च अनादरे (२.३.३८)।",
    anuvritti_from        = ('2.3.50',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
