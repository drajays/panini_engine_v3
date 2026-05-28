"""
2.1.43  कृत्यैर्ऋणे  —  VIDHI

Padaccheda: कृत्यैः ऋणे

krtya words in rna (debt) context with saptami form tatpurusha.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_43_krtya_rne"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyErfRe",
    text_dev              = "कृत्यैर्ऋणे",
    padaccheda_dev        = "कृत्यैः ऋणे",
    why_dev               = "कृत्यैः ऋणे सप्तम्यन्तस्य सह तत्पुरुषः (२.१.४३)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
