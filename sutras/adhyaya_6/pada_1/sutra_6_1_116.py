"""
6.1.116  अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च  —  VIDHI

Padaccheda: अव्यात्-अवद्यात्-अवक्रमुः-अव्रत-अयम्-अवन्तु-अवस्युषु च

अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च (6.1.116)
Pāṭha: ashtadhyayi.com data.txt row i=61116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_116_avyAdavady_116"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.116", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avyAdavadyAdavakramuravratAyamavantvavasyuzu ca",
    text_dev              = "अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च",
    samagra_slp1          = "saMhitAyAm avyAt-avadyAt-avakramuH-avrata-ayam-avantu-avasyuzu ca aci antaHpAdam prakftyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् अव्यात्-अवद्यात्-अवक्रमुः-अव्रत-अयम्-अवन्तु-अवस्युषु च अचि अन्तःपादम् प्रकृत्या",
    padaccheda_dev        = "अव्यात्-अवद्यात्-अवक्रमुः-अव्रत-अयम्-अवन्तु-अवस्युषु च",
    why_dev               = "(सूत्रम् 6.1.116) अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
