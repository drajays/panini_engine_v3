"""
6.1.53  अपगुरो णमुलि  —  VIDHI

Padaccheda: अपगुरः णमुँल्ि

अपगुरो णमुलि (6.1.53)
Pāṭha: ashtadhyayi.com data.txt row i=61053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_53_apaguro_53"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.53", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apaguro Ramuli",
    text_dev              = "अपगुरो णमुलि",
    samagra_slp1          = "apaguraH Ramuli At ecaH upadeSe viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अपगुरः णमुलि आत् एचः उपदेशे विभाषा",
    padaccheda_dev        = "अपगुरः णमुँल्ि",
    why_dev               = "(सूत्रम् 6.1.53) अपगुरो णमुलि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
