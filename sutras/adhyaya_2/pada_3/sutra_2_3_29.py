"""
2.3.29  अन्यारादितरर्तेदिक्छब्दाञ्चूत्तरपदाजाहियुक्ते  —  VIDHI

Padaccheda: अन्य-आरात्-इतर-ऋते-दिक्शब्द-अञ्चु-उत्तरपद-आच्-आहियुक्ते

anya, arat, itara, rte, dik-words, ancu, ac, ahi take pancami.
Pāṭha: ashtadhyayi.com data.txt row i=23029 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_29_anya_arat_dik"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'anyArAditarartedikCabdAYcUttarapadAjAhiyukte',
    text_dev              = 'अन्यारादितरर्तेदिक्छब्दाञ्चूत्तरपदाजाहियुक्ते',
    samagra_slp1          = "anaBihite anya-ArAt-itara-fte-dik-Sabda-aYcu-uttarapada-Ac-Ahiyukte paYcamI",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते अन्य-आरात्-इतर-ऋते-दिक्-शब्द-अञ्चु-उत्तरपद-आच्-आहियुक्ते पञ्चमी",
    padaccheda_dev        = "अन्य-आरात्-इतर-ऋते-दिक्शब्द-अञ्चु-उत्तरपद-आच्-आहियुक्ते",
    why_dev               = "अन्य-आरात्-इतर-ऋते-दिक्-अञ्चु-आच्-आहियुक्ते पञ्चमी (२.३.२९)।",
    anuvritti_from        = ('2.3.28',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
