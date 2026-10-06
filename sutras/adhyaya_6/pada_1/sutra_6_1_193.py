"""
6.1.193  लिति  —  VIDHI

Padaccheda: लिति

लिति (6.1.193)
Pāṭha: ashtadhyayi.com data.txt row i=61193 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_193_liti_193"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.193", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.193"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.193",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liti",
    text_dev              = "लिति",
    samagra_slp1          = "liti pratyayAt pUrvamudAttaH",
    samagra_dev           = "लिति प्रत्ययात् पूर्वमुदात्तः",
    padaccheda_dev        = "लिति",
    why_dev               = "(सूत्रम् 6.1.193) लिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
