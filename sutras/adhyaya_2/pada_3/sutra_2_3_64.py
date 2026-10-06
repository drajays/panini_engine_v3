"""
2.3.64  कृत्वोऽर्थप्रयोगे कालेऽधिकरणे  —  VIDHI

Padaccheda: कृत्वः-अर्थ-प्रयोगे काले अधिकरणे

In krtvas-artha (num-times) usage, time takes saptami.
Pāṭha: ashtadhyayi.com data.txt row i=23064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_64_krtvas_kala"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'kftvorTaprayoge kAleDikaraRe',
    text_dev              = 'कृत्वोऽर्थप्रयोगे कालेऽधिकरणे',
    samagra_slp1          = "anaBihite kftvorTa-prayoge kAle aDikaraRe Seze zazWI",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते कृत्वोऽर्थ-प्रयोगे काले अधिकरणे शेषे षष्ठी",
    padaccheda_dev        = "कृत्वः-अर्थ-प्रयोगे काले अधिकरणे",
    why_dev               = "कृत्वः-अर्थ-प्रयोगे काले अधिकरणे (२.३.६४)।",
    anuvritti_from        = ('2.3.36',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
