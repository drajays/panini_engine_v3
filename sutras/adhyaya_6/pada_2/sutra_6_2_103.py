"""
6.2.103  दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु  —  VIDHI

Padaccheda: दिक्शब्दाः ग्राम-जनपद-आख्यान-चानराटेषु

दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु (6.2.103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_103_dikSabdA_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dikSabdA grAmajanapadAKyAnacAnarAwezu",
    text_dev              = "दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु",
    padaccheda_dev        = "दिक्शब्दाः ग्राम-जनपद-आख्यान-चानराटेषु",
    why_dev               = "(सूत्रम् 6.2.103) दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
