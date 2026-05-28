"""
6.3.71  श्येनतिलस्य पाते ञे  —  VIDHI

Padaccheda: श्येन-तिलस्य पाते ञे

श्येनतिलस्य पाते ञे (6.3.71)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_3_71_Syenatilas_71"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Syenatilasya pAte Ye",
    text_dev              = "श्येनतिलस्य पाते ञे",
    padaccheda_dev        = "श्येन-तिलस्य पाते ञे",
    why_dev               = "(सूत्रम् 6.3.71) श्येनतिलस्य पाते ञे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
