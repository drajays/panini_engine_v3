"""
6.4.12  इन्हन्पूषार्यम्णां शौ  —  VIDHI

Padaccheda: इन्-हन्-पूष-अर्यम्णाम् शौ

इन्हन्पूषार्यम्णां शौ (6.4.12)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_12_inhanpUzAr_12"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.12", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "inhanpUzAryamRAM SO",
    text_dev              = "इन्हन्पूषार्यम्णां शौ",
    padaccheda_dev        = "इन्-हन्-पूष-अर्यम्णाम् शौ",
    why_dev               = "(सूत्रम् 6.4.12) इन्हन्पूषार्यम्णां शौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
