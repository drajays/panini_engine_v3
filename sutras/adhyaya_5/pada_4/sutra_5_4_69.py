"""
5.4.69  न पूजनात्  —  VIDHI

Padaccheda: न पूजनात्

न पूजनात् (5.4.69)
Pāṭha: ashtadhyayi.com data.txt row i=54069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_69_na_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.69", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.69",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na pUjanAt",
    text_dev              = "न पूजनात्",
    samagra_slp1          = "samAsAntAH pUjanAt na",
    samagra_dev           = "समासान्ताः पूजनात् न",
    padaccheda_dev        = "न पूजनात्",
    why_dev               = "(सूत्रम् 5.4.69) न पूजनात्।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
