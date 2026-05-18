"""
4.1.26  संख्याऽव्ययादेर्ङीप्  —  VIDHI

Padaccheda: संख्या-अव्यय-आदेः ङीप्

संख्याऽव्ययादेर्ङीप् (4.1.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_26_saMKyAvya_26"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_26_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyA'vyayAderNIp",
    text_dev              = "संख्याऽव्ययादेर्ङीप्",
    padaccheda_dev        = "संख्या-अव्यय-आदेः ङीप्",
    why_dev               = "(सूत्रम् 4.1.26) संख्याऽव्ययादेर्ङीप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
