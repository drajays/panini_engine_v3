"""
6.4.169  आत्माध्वानौ खे  —  VIDHI

Padaccheda: आत्म-अध्वानौ खे

आत्माध्वानौ खे (6.4.169)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_169_AtmADvAnO_169"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_169_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.169"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.169",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmADvAnO Ke",
    text_dev              = "आत्माध्वानौ खे",
    padaccheda_dev        = "आत्म-अध्वानौ खे",
    why_dev               = "(सूत्रम् 6.4.169) आत्माध्वानौ खे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
