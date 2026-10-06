"""
6.2.110  निष्ठोपसर्गपूर्वमन्यतरस्याम्  —  VIDHI

Padaccheda: निष्ठा उपसर्ग-पूर्वम् अन्यतरस्याम्

निष्ठोपसर्गपूर्वमन्यतरस्याम् (6.2.110)
Pāṭha: ashtadhyayi.com data.txt row i=62110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_110_nizWopasar_110"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.110", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.110",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWopasargapUrvamanyatarasyAm",
    text_dev              = "निष्ठोपसर्गपूर्वमन्यतरस्याम्",
    samagra_slp1          = "udAttaH antaH nizWA upasargapUrvam anyatarasyAm bahuvrIhO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः अन्तः निष्ठा उपसर्गपूर्वम् अन्यतरस्याम् बहुव्रीहौ",
    padaccheda_dev        = "निष्ठा उपसर्ग-पूर्वम् अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.2.110) निष्ठोपसर्गपूर्वमन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
