"""
4.4.27  ओजस्सहोऽम्भसा वर्तते  —  VIDHI

Padaccheda: ओजः-सहः-अम्भसा वर्तते (क्रियापदम्)

ओजस्सहोऽम्भसा वर्तते (4.4.27)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_27_ojassahom_27"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ojassaho'mBasA vartate",
    text_dev              = "ओजस्सहोऽम्भसा वर्तते",
    padaccheda_dev        = "ओजः-सहः-अम्भसा वर्तते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.27) ओजस्सहोऽम्भसा वर्तते।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
