"""
5.4.43  संख्यैकवचनाच्च वीप्सायाम्  —  VIDHI

Padaccheda: सङ्ख्या-एकवचनात् च वीप्सायाम्

संख्यैकवचनाच्च वीप्सायाम् (5.4.43)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_43_saMKyEkava_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_43_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyEkavacanAcca vIpsAyAm",
    text_dev              = "संख्यैकवचनाच्च वीप्सायाम्",
    padaccheda_dev        = "सङ्ख्या-एकवचनात् च वीप्सायाम्",
    why_dev               = "(सूत्रम् 5.4.43) संख्यैकवचनाच्च वीप्सायाम्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
