"""
6.2.142  नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु  —  VIDHI

Padaccheda: न उत्तरपदे अनुदात्त-आदौ अ-पृथिवी-रुद्र-पूष-मन्थिषु

नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु (6.2.142)
Pāṭha: ashtadhyayi.com data.txt row i=62142 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_142_nottarapad_142"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.142", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.142"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.142",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'nottarapadenudAttAdAvapfTivIrudrapUzamanTizu',
    text_dev              = 'नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु',
    samagra_slp1          = "uttarapadAdiH na uttarapade anudAttAdO a-pfTivI-rudra-pUzamanTizu prakftyA uBe yugapat devatAdvandve",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः न उत्तरपदे अनुदात्तादौ अ-पृथिवी-रुद्र-पूषमन्थिषु प्रकृत्या उभे युगपत् देवताद्वन्द्वे",
    padaccheda_dev        = "न उत्तरपदे अनुदात्त-आदौ अ-पृथिवी-रुद्र-पूष-मन्थिषु",
    why_dev               = "(सूत्रम् 6.2.142) नोत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
