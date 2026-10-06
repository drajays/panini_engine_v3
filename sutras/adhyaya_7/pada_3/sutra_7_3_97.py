"""
7.3.97  बहुलं छन्दसि  —  VIDHI

Padaccheda: बहुलम् छन्दसि

बहुलं छन्दसि (7.3.97)
Pāṭha: ashtadhyayi.com data.txt row i=73097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_97_bahulaM_97"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.97", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahulaM Candasi",
    text_dev              = "बहुलं छन्दसि",
    samagra_slp1          = "Candasi astisicaH aNgAt apfkte sArvaDAtuke hali Iw bahulam",
    samagra_dev           = "छन्दसि अस्तिसिचः अङ्गात् अपृक्ते सार्वधातुके हलि ईट् बहुलम्",
    padaccheda_dev        = "बहुलम् छन्दसि",
    why_dev               = "(सूत्रम् 7.3.97) बहुलं छन्दसि।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
