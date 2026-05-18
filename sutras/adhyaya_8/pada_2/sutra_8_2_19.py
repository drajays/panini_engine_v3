"""
8.2.19  उपसर्गस्यायतौ  —  VIDHI

Padaccheda: उपसर्गस्य अयतौ

उपसर्गस्यायतौ (8.2.19)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_19_upasargasy_19"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_19_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.19",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargasyAyatO",
    text_dev              = "उपसर्गस्यायतौ",
    padaccheda_dev        = "उपसर्गस्य अयतौ",
    why_dev               = "(सूत्रम् 8.2.19) उपसर्गस्यायतौ।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
