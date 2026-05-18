"""
6.4.112  श्नाऽभ्यस्तयोरातः  —  VIDHI

Padaccheda: श्ना-अभ्यस्तयोः आतः

श्नाऽभ्यस्तयोरातः (6.4.112)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_112_SnAByasta_112"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_112_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.112"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.112",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SnA'ByastayorAtaH",
    text_dev              = "श्नाऽभ्यस्तयोरातः",
    padaccheda_dev        = "श्ना-अभ्यस्तयोः आतः",
    why_dev               = "(सूत्रम् 6.4.112) श्नाऽभ्यस्तयोरातः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
