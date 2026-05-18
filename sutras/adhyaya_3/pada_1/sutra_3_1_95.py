"""
3.1.95  कृत्याः प्राङ् ण्वुलः  —  VIDHI

Padaccheda: कृत्याः प्राङ् ण्वुलः

Krt suffix rule from dhatu: कृत्याः प्राङ् ण्वुलः (95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_95_kftyAH_95"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_95_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyAH prAN RvulaH",
    text_dev              = "कृत्याः प्राङ् ण्वुलः",
    padaccheda_dev        = "कृत्याः प्राङ् ण्वुलः",
    why_dev               = "धातोः [कृत्याः प्राङ् ण्वुलः]-प्रत्ययः विहितः (३.१.95)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
