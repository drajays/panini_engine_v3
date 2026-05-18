"""
4.2.137  गर्तोत्तरपदाच्छः  —  VIDHI

Padaccheda: गर्त-उत्तरपदात् छः

गर्तोत्तरपदाच्छः (4.2.137)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_137_gartottara_137"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_137_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "gartottarapadAcCaH",
    text_dev              = "गर्तोत्तरपदाच्छः",
    padaccheda_dev        = "गर्त-उत्तरपदात् छः",
    why_dev               = "(सूत्रम् 4.2.137) गर्तोत्तरपदाच्छः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
