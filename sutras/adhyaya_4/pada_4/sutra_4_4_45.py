"""
4.4.45  सेनाया वा  —  VIDHI

Padaccheda: सेनायाः वा

सेनाया वा (4.4.45)
Pāṭha: ashtadhyayi.com data.txt row i=44045 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_45_senAyA_45"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.45", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.45"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.45",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "senAyA vA",
    text_dev              = "सेनाया वा",
    samagra_slp1          = "tat samavAyAn samavEti iti senAyAH RyaH Wak vA",
    samagra_dev           = "'तत् समवायान् समवैति' (इति) सेनायाः ण्यः ठक् वा",
    padaccheda_dev        = "सेनायाः वा",
    why_dev               = "(सूत्रम् 4.4.45) सेनाया वा।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
