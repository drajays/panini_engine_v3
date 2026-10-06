"""
6.2.114  कण्ठपृष्ठग्रीवाजंघं च  —  VIDHI

Padaccheda: कण्ठ-पृष्ठ-ग्रीवा-जंघम् च

कण्ठपृष्ठग्रीवाजंघं च (6.2.114)
Pāṭha: ashtadhyayi.com data.txt row i=62114 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_114_kaRWapfzWa_114"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.114", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaRWapfzWagrIvAjaMGaM ca",
    text_dev              = "कण्ठपृष्ठग्रीवाजंघं च",
    samagra_slp1          = "udAttaH uttarapadAdiH kaRWa-pfzWa-grIvA-jaMGam ca bahuvrIhO saMjYA-OpamyayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः कण्ठ-पृष्ठ-ग्रीवा-जंघम् च बहुव्रीहौ संज्ञा-औपम्ययोः",
    padaccheda_dev        = "कण्ठ-पृष्ठ-ग्रीवा-जंघम् च",
    why_dev               = "(सूत्रम् 6.2.114) कण्ठपृष्ठग्रीवाजंघं च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
