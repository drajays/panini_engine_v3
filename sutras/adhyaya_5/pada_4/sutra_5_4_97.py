"""
5.4.97  उपमानादप्राणिषु  —  VIDHI

Padaccheda: उपमानात् अप्राणिषु

उपमानादप्राणिषु (5.4.97)
Pāṭha: ashtadhyayi.com data.txt row i=54097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_97_upamAnAdap_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.97", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upamAnAdaprARizu",
    text_dev              = "उपमानादप्राणिषु",
    samagra_slp1          = "tatpuruzasya SunaH upamAnAt aprARizu wac",
    samagra_dev           = "तत्पुरुषस्य शुनः उपमानात् अप्राणिषु टच्",
    padaccheda_dev        = "उपमानात् अप्राणिषु",
    why_dev               = "(सूत्रम् 5.4.97) उपमानादप्राणिषु।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
