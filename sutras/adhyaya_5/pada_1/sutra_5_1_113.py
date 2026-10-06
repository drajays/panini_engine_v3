"""
5.1.113  ऐकागारिकट् चौरे  —  VIDHI

Padaccheda: ऐकागारिकट् चौरे

ऐकागारिकट् चौरे (5.1.113)
Pāṭha: ashtadhyayi.com data.txt row i=51113 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_113_EkAgArikaw_113"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.113", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.113"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.113",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "EkAgArikaw cOre",
    text_dev              = "ऐकागारिकट् चौरे",
    samagra_slp1          = "cOre EkAgArikaw nipAtyate",
    samagra_dev           = "चौरे ऐकागारिकट् (निपात्यते)",
    padaccheda_dev        = "ऐकागारिकट् चौरे",
    why_dev               = "(सूत्रम् 5.1.113) ऐकागारिकट् चौरे।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
