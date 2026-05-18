"""
2.4.10  शूद्राणामनिरवसितानाम्  —  VIDHI

Padaccheda: शूद्राणाम् अनिरवसितानाम्

dvandva of shudra non-outcaste groups.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_10_sudra_aniravasita"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_10_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SUdrARAmaniravasitAnAm",
    text_dev              = "शूद्राणामनिरवसितानाम्",
    padaccheda_dev        = "शूद्राणाम् अनिरवसितानाम्",
    why_dev               = "शूद्राणाम् अनिरवसितानां द्वन्द्वे (२.४.१०)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
