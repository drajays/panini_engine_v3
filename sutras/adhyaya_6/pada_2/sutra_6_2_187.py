"""
6.2.187  स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च  —  VIDHI

Padaccheda: स्फिग-पूत-वीणा-अञ्जः-अध्व-कुक्षि-सीरनाम-नाम च

स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च (6.2.187)
Pāṭha: ashtadhyayi.com data.txt row i=62187 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_187_sPigapUtav_187"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.187", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.187"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.187",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'sPigapUtavIRAYjoDvakukzisIranAmanAma ca',
    text_dev              = 'स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च',
    samagra_slp1          = "uttarapadAdiH antaH sPiga-pUta-vIRA-aYjas-aDvan-kukzi-sIranAma-nAma ca upasargAt apAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः स्फिग-पूत-वीणा-अञ्जस्-अध्वन्-कुक्षि-सीरनाम-नाम च उपसर्गात् अपात्",
    padaccheda_dev        = "स्फिग-पूत-वीणा-अञ्जः-अध्व-कुक्षि-सीरनाम-नाम च",
    why_dev               = "(सूत्रम् 6.2.187) स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
