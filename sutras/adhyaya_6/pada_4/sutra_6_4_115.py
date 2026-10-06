"""
6.4.115  भियोऽन्यतरस्याम्  —  VIDHI

Padaccheda: भियः अन्यतरस्याम्

भियोऽन्यतरस्याम् (6.4.115)
Pāṭha: ashtadhyayi.com data.txt row i=64115 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_115_Biyonyata_115"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.115", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'BiyonyatarasyAm',
    text_dev              = 'भियोऽन्यतरस्याम्',
    samagra_slp1          = "BiyaH aNgasya hali sArvaDAtuke kNiti it anyatarasyAm",
    samagra_dev           = "भियः अङ्गस्य हलि सार्वधातुके क्ङिति इत् अन्यतरस्याम्",
    padaccheda_dev        = "भियः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.4.115) भियोऽन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
