"""
8.2.4  उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य  —  VIDHI

Padaccheda: उदात्त-स्वरितयोः यणः स्वरितः अनुदात्तस्य

उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य (8.2.4)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_4_udAttasvar_4"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_2_4_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udAttasvaritayoryaRaH svarito'nudAttasya",
    text_dev              = "उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य",
    padaccheda_dev        = "उदात्त-स्वरितयोः यणः स्वरितः अनुदात्तस्य",
    why_dev               = "(सूत्रम् 8.2.4) उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
