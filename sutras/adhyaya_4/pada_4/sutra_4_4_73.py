"""
4.4.73  निकटे वसति  —  VIDHI

Padaccheda: निकटे वसति (क्रियापदम्)

निकटे वसति (4.4.73)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_73_nikawe_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_73_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nikawe vasati",
    text_dev              = "निकटे वसति",
    padaccheda_dev        = "निकटे वसति (क्रियापदम्)",
    why_dev               = "(सूत्रम् 4.4.73) निकटे वसति।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
