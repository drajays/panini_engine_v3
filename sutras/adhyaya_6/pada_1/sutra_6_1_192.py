"""
6.1.192  भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति  —  VIDHI

Padaccheda: भी-ह्री-भृ-हु-मद-जन-धन-दरिद्रा-जागराम् प्रत्ययात् पूर्वम् प्-इति

भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति (6.1.192)
Pāṭha: ashtadhyayi.com data.txt row i=61192 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_192_BIhrIBfhum_192"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.192", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.192"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.192",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BIhrIBfhumadajanaDanadaridrAjAgarAM pratyayAt pUrvam piti",
    text_dev              = "भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति",
    samagra_slp1          = "BI-hrI-Bf-hu-mada-jana-Dana-daridrA-jAgarAm pratyayAt pUrvam piti udAttaH la-sArvaDAtukam aByastAnAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "भी-ह्री-भृ-हु-मद-जन-धन-दरिद्रा-जागराम् प्रत्ययात् पूर्वम् पिति उदात्तः ल-सार्वधातुकम् अभ्यस्तानाम्",
    padaccheda_dev        = "भी-ह्री-भृ-हु-मद-जन-धन-दरिद्रा-जागराम् प्रत्ययात् पूर्वम् प्-इति",
    why_dev               = "(सूत्रम् 6.1.192) भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
