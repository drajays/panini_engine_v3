"""
4.4.36  परिपन्थं च तिष्ठति  —  VIDHI

Padaccheda: परिपन्थम् च तिष्ठति (क्रियापदम्)

परिपन्थं च तिष्ठति (4.4.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_36_paripanTaM_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paripanTaM ca tizWati",
    text_dev              = "परिपन्थं च तिष्ठति",
    padaccheda_dev        = "परिपन्थम् च तिष्ठति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.36) परिपन्थं च तिष्ठति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
