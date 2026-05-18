"""
6.2.83  अन्त्यात् पूर्वं बह्वचः  —  VIDHI

Padaccheda: अन्त्यात् पूर्वम् बहु-अचः

अन्त्यात् पूर्वं बह्वचः (6.2.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_83_antyAt_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_83_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antyAt pUrvaM bahvacaH",
    text_dev              = "अन्त्यात् पूर्वं बह्वचः",
    padaccheda_dev        = "अन्त्यात् पूर्वम् बहु-अचः",
    why_dev               = "(सूत्रम् 6.2.83) अन्त्यात् पूर्वं बह्वचः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
