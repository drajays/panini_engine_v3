"""
4.1.120  स्त्रीभ्यो ढक्  —  VIDHI

Padaccheda: स्त्रीभ्यः ढक्

स्त्रीभ्यो ढक् (4.1.120)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_120_strIByo_120"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_120_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.120"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "strIByo Qak",
    text_dev              = "स्त्रीभ्यो ढक्",
    padaccheda_dev        = "स्त्रीभ्यः ढक्",
    why_dev               = "(सूत्रम् 4.1.120) स्त्रीभ्यो ढक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
