"""
5.4.90  उत्तमैकाभ्यां च  —  VIDHI

Padaccheda: उत्तम-एकाभ्याम् च

उत्तमैकाभ्यां च (5.4.90)
Pāṭha: ashtadhyayi.com data.txt row i=54090 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_90_uttamEkABy_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.90", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttamEkAByAM ca",
    text_dev              = "उत्तमैकाभ्यां च",
    samagra_slp1          = "uttama-ekAByAmahnaH ahnaH na",
    samagra_dev           = "उत्तम-एकाभ्यामह्नः अह्नः न",
    padaccheda_dev        = "उत्तम-एकाभ्याम् च",
    why_dev               = "(सूत्रम् 5.4.90) उत्तमैकाभ्यां च।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
