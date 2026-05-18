"""
4.2.73  बह्वचः कूपेषु  —  VIDHI

Padaccheda: बहु-अचः कूपेषु

बह्वचः कूपेषु (4.2.73)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_73_bahvacaH_73"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_73_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.73"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.73",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahvacaH kUpezu",
    text_dev              = "बह्वचः कूपेषु",
    padaccheda_dev        = "बहु-अचः कूपेषु",
    why_dev               = "(सूत्रम् 4.2.73) बह्वचः कूपेषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
