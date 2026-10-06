"""
6.4.127  अर्वणस्त्रसावनञः  —  VIDHI

Padaccheda: अर्वणः तृ (लुप्तप्रथमान्तनिर्देशः) अ-सौ अन्-अञः

अर्वणस्त्रसावनञः (6.4.127)
Pāṭha: ashtadhyayi.com data.txt row i=64127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_127_arvaRastra_127"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.127", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "arvaRastrasAvanaYaH",
    text_dev              = "अर्वणस्त्रसावनञः",
    samagra_slp1          = "aNgasya asidDavadatrABAt arvaRaH tf asO anaYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् अर्वणः तृ असौ अनञः",
    padaccheda_dev        = "अर्वणः तृ (लुप्तप्रथमान्तनिर्देशः) अ-सौ अन्-अञः",
    why_dev               = "(सूत्रम् 6.4.127) अर्वणस्त्रसावनञः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
