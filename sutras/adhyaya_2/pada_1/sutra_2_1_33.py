"""
2.1.33  कृत्यैरधिकार्थवचने  —  VIDHI

Padaccheda: कृत्यैः अधिक-अर्थ-वचने

krtya words with adhikaartha-vacana form tatpurusha compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_33_krtya_adhika"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("tatpurusha" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.1.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kftyEraDikArTavacane",
    text_dev              = "कृत्यैरधिकार्थवचने",
    padaccheda_dev        = "कृत्यैः अधिक-अर्थ-वचने",
    why_dev               = "कृत्यैः अधिक-अर्थ-वचने तत्पुरुषः (२.१.३३)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
