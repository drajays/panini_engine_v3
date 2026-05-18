"""
5.2.40  किमिदंभ्यां वो घः  —  VIDHI

Padaccheda: किम्-इदम्भ्याम् वः घः

किमिदंभ्यां वो घः (5.2.40)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_40_kimidaMByA_40"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_40_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kimidaMByAM vo GaH",
    text_dev              = "किमिदंभ्यां वो घः",
    padaccheda_dev        = "किम्-इदम्भ्याम् वः घः",
    why_dev               = "(सूत्रम् 5.2.40) किमिदंभ्यां वो घः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
