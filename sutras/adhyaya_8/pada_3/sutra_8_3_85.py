"""
8.3.85  मातुःपितुर्भ्यामन्यतरस्याम्  —  VIDHI

Padaccheda: मातुः-पितुर्भ्याम् अन्यतरस्याम्

मातुःपितुर्भ्यामन्यतरस्याम् (8.3.85)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_85_mAtuHpitur_85"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_85_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.85"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAtuHpiturByAmanyatarasyAm",
    text_dev              = "मातुःपितुर्भ्यामन्यतरस्याम्",
    padaccheda_dev        = "मातुः-पितुर्भ्याम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 8.3.85) मातुःपितुर्भ्यामन्यतरस्याम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
