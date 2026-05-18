"""
4.3.61  ग्रामात् पर्यनुपूर्वात्  —  VIDHI

Padaccheda: ग्रामात् परि-अनु-पूर्वात्

ग्रामात् पर्यनुपूर्वात् (4.3.61)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_61_grAmAt_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_61_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmAt paryanupUrvAt",
    text_dev              = "ग्रामात् पर्यनुपूर्वात्",
    padaccheda_dev        = "ग्रामात् परि-अनु-पूर्वात्",
    why_dev               = "(सूत्रम् 4.3.61) ग्रामात् पर्यनुपूर्वात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
