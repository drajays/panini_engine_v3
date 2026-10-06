"""
5.1.107  कालाद्यत्  —  VIDHI

Padaccheda: कालात् यत्

कालाद्यत् (5.1.107)
Pāṭha: ashtadhyayi.com data.txt row i=51107 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_107_kAlAdyat_107"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.107", state, "5.1.18"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.107"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.107",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAlAdyat",
    text_dev              = "कालाद्यत्",
    samagra_slp1          = "tat asya prAptam iti kAlAt yat",
    samagra_dev           = "'तत् अस्य प्राप्तम्' (इति) कालात् यत्",
    padaccheda_dev        = "कालात् यत्",
    why_dev               = "(सूत्रम् 5.1.107) कालाद्यत्।",
    anuvritti_from        = ('5.1.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
