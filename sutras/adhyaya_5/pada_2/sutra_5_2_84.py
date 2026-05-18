"""
5.2.84  श्रोत्रियंश्छन्दोऽधीते  —  VIDHI

Padaccheda: श्रोत्रियन् छन्दः अधीते (क्रियापदम्)

श्रोत्रियंश्छन्दोऽधीते (5.2.84)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_84_SrotriyaMS_84"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_84_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SrotriyaMSCando'DIte",
    text_dev              = "श्रोत्रियंश्छन्दोऽधीते",
    padaccheda_dev        = "श्रोत्रियन् छन्दः अधीते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 5.2.84) श्रोत्रियंश्छन्दोऽधीते।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
