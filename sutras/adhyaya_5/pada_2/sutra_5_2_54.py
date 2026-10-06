"""
5.2.54  द्वेस्तीयः  —  VIDHI

Padaccheda: द्वेः तीयः

द्वेस्तीयः (5.2.54)
Pāṭha: ashtadhyayi.com data.txt row i=52054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_54_dvestIyaH_54"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.54", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dvestIyaH",
    text_dev              = "द्वेस्तीयः",
    samagra_slp1          = "tasya pUraRe iti dveH tIyaH",
    samagra_dev           = "'तस्य पूरणे' (इति) द्वेः तीयः",
    padaccheda_dev        = "द्वेः तीयः",
    why_dev               = "(सूत्रम् 5.2.54) द्वेस्तीयः।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
