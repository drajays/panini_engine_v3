"""
4.1.87  स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्  —  VIDHI

Padaccheda: स्त्री-पुंसाभ्याम् नञ्-स्नञौ भवनात्

स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात् (4.1.87)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_87_strIpuMsAB_87"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_87_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.87"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.87",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "strIpuMsAByAM naYsnaYO BavanAt",
    text_dev              = "स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्",
    padaccheda_dev        = "स्त्री-पुंसाभ्याम् नञ्-स्नञौ भवनात्",
    why_dev               = "(सूत्रम् 4.1.87) स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
