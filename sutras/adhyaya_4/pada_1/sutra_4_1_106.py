"""
4.1.106  मधुबभ्र्वोर्ब्राह्मणकौशिकयोः  —  VIDHI

Padaccheda: मधु-बभ्र्वोः ब्राह्मण-कौशिकयोः

मधुबभ्र्वोर्ब्राह्मणकौशिकयोः (4.1.106)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_106_maDubaBrvo_106"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_106_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.106"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.106",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "maDubaBrvorbrAhmaRakOSikayoH",
    text_dev              = "मधुबभ्र्वोर्ब्राह्मणकौशिकयोः",
    padaccheda_dev        = "मधु-बभ्र्वोः ब्राह्मण-कौशिकयोः",
    why_dev               = "(सूत्रम् 4.1.106) मधुबभ्र्वोर्ब्राह्मणकौशिकयोः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
