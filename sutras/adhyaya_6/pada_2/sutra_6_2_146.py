"""
6.2.146  संज्ञायामनाचितादीनाम्  —  VIDHI

Padaccheda: संज्ञायाम् अनाचित-आदीनाम्

संज्ञायामनाचितादीनाम् (6.2.146)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_146_saMjYAyAma_146"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMjYAyAmanAcitAdInAm",
    text_dev              = "संज्ञायामनाचितादीनाम्",
    padaccheda_dev        = "संज्ञायाम् अनाचित-आदीनाम्",
    why_dev               = "(सूत्रम् 6.2.146) संज्ञायामनाचितादीनाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
