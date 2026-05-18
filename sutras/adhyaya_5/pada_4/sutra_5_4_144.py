"""
5.4.144  विभाषा श्यावारोकाभ्याम्  —  VIDHI

Padaccheda: विभाषा श्याव-अरोकाभ्याम्

विभाषा श्यावारोकाभ्याम् (5.4.144)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_144_viBAzA_144"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_144_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA SyAvArokAByAm",
    text_dev              = "विभाषा श्यावारोकाभ्याम्",
    padaccheda_dev        = "विभाषा श्याव-अरोकाभ्याम्",
    why_dev               = "(सूत्रम् 5.4.144) विभाषा श्यावारोकाभ्याम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
