"""
6.2.135  षट् च काण्डादीनि  —  VIDHI

Padaccheda: षट् च काण्ड-आदीनि

षट् च काण्डादीनि (6.2.135)
Pāṭha: ashtadhyayi.com data.txt row i=62135 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_135_zaw_135"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.135", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.135"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "zaw ca kARqAdIni",
    text_dev              = "षट् च काण्डादीनि",
    samagra_slp1          = "udAttaH uttarapadAdiH zaw ca kARqAdIni tatpuruze a-prARi-zazWyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः षट् च काण्डादीनि तत्पुरुषे अ-प्राणि-षष्ठ्याः",
    padaccheda_dev        = "षट् च काण्ड-आदीनि",
    why_dev               = "(सूत्रम् 6.2.135) षट् च काण्डादीनि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
