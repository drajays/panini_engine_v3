"""
3.4.91  सवाभ्यां वामौ  —  VIDHI

Padaccheda: स-वाभ्याम् वा-मौ

krt-suffix rule: सवाभ्यां वामौ
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_91_savAByAM_91"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_4_91_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.91"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.91",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "savAByAM vAmO",
    text_dev              = "सवाभ्यां वामौ",
    padaccheda_dev        = "स-वाभ्याम् वा-मौ",
    why_dev               = "धातोः प्रत्ययः (३.4.91)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
