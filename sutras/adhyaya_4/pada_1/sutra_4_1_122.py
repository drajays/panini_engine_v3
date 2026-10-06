"""
4.1.122  इतश्चानिञः  —  VIDHI

Padaccheda: इतः च अन्-इञः

इतश्चानिञः (4.1.122)
Pāṭha: ashtadhyayi.com data.txt row i=41122 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_122_itaScAniYa_122"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.122", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.122"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.122",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "itaScAniYaH",
    text_dev              = "इतश्चानिञः",
    samagra_slp1          = "tasya apatyam iti aniYaH dvyacaH itaH Qak",
    samagra_dev           = "'तस्य अपत्यम्' (इति) अनिञः द्व्यचः इतः ढक्",
    padaccheda_dev        = "इतः च अन्-इञः",
    why_dev               = "(सूत्रम् 4.1.122) इतश्चानिञः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
