"""
5.1.97  व्युष्टादिभ्योऽण्  —  VIDHI

Padaccheda: व्युष्ट-आदिभ्यः अण्

व्युष्टादिभ्योऽण् (5.1.97)
Pāṭha: ashtadhyayi.com data.txt row i=51097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_97_vyuzwAdiBy_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.97", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'vyuzwAdiByoR',
    text_dev              = 'व्युष्टादिभ्योऽण्',
    samagra_slp1          = "tatra dIyate kAryam iti vyuzwAdiByaH aR",
    samagra_dev           = "'तत्र दीयते, कार्यम्' (इति) व्युष्टादिभ्यः अण्",
    padaccheda_dev        = "व्युष्ट-आदिभ्यः अण्",
    why_dev               = "(सूत्रम् 5.1.97) व्युष्टादिभ्योऽण्।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
