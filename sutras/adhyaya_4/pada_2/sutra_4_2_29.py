"""
4.2.29  महेन्द्राद्घाणौ च  —  VIDHI

Padaccheda: महेन्द्रात् घ-अणौ च

महेन्द्राद्घाणौ च (4.2.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_29_mahendrAdG_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mahendrAdGARO ca",
    text_dev              = "महेन्द्राद्घाणौ च",
    padaccheda_dev        = "महेन्द्रात् घ-अणौ च",
    why_dev               = "(सूत्रम् 4.2.29) महेन्द्राद्घाणौ च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
