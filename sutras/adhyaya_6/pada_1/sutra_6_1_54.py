"""
6.1.54  चिस्फुरोर्णौ  —  VIDHI

Padaccheda: चि-स्फुरोः णौ

चिस्फुरोर्णौ (6.1.54)
Pāṭha: ashtadhyayi.com data.txt row i=61054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_54_cisPurorRO_54"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.54", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cisPurorRO",
    text_dev              = "चिस्फुरोर्णौ",
    samagra_slp1          = "ci-sPuroH RO At ecaH upadeSe viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "चि-स्फुरोः णौ आत् एचः उपदेशे विभाषा",
    padaccheda_dev        = "चि-स्फुरोः णौ",
    why_dev               = "(सूत्रम् 6.1.54) चिस्फुरोर्णौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
