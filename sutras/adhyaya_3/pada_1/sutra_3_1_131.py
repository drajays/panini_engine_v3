"""
3.1.131  अग्नौ परिचाय्योपचाय्यसमूह्याः  —  VIDHI

Padaccheda: अग्नौ परिचाय्य-उपचाय्य-समूह्याः

Krt suffix rule from dhatu: अग्नौ परिचाय्योपचाय्यसमूह्याः (131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_131_agnO_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_131_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agnO paricAyyopacAyyasamUhyAH",
    text_dev              = "अग्नौ परिचाय्योपचाय्यसमूह्याः",
    padaccheda_dev        = "अग्नौ परिचाय्य-उपचाय्य-समूह्याः",
    why_dev               = "धातोः [अग्नौ परिचाय्योपचाय्यसमूह्याः]-प्रत्ययः विहितः (३.१.131)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
