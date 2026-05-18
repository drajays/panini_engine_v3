"""
5.4.94  अनोऽश्मायस्सरसाम् जातिसंज्ञयोः  —  VIDHI

Padaccheda: अनः-अश्म-अयः-सरसाम् जाति-संज्ञयोः

अनोऽश्मायस्सरसाम् जातिसंज्ञयोः (5.4.94)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_94_anoSmAyas_94"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_94_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.94"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.94",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ano'SmAyassarasAm jAtisaMjYayoH",
    text_dev              = "अनोऽश्मायस्सरसाम् जातिसंज्ञयोः",
    padaccheda_dev        = "अनः-अश्म-अयः-सरसाम् जाति-संज्ञयोः",
    why_dev               = "(सूत्रम् 5.4.94) अनोऽश्मायस्सरसाम् जातिसंज्ञयोः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
