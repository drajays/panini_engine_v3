"""
6.2.38  महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु  —  VIDHI

Padaccheda: महान् व्रीहि-अपराह्ण-गृष्टि-इष्वास-जाबाल-भार-भारत-हैलि-हिल-रौरव-प्रवृद्धेषु

महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु (6.2.38)
Pāṭha: ashtadhyayi.com data.txt row i=62038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_38_mahAn_38"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.38", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mahAn vrIhyaparAhRagfzwIzvAsajAbAlaBAraBAratahElihilarOravapravfdDezu",
    text_dev              = "महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु",
    samagra_slp1          = "mahAn vrIhi-aparAhRa-gfzwi-izvAsa-jAbAla-BAra-BArata-hElihila-rOrava-pravfdDezu prakftyA pUrvapadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "महान् व्रीहि-अपराह्ण-गृष्टि-इष्वास-जाबाल-भार-भारत-हैलिहिल-रौरव-प्रवृद्धेषु प्रकृत्या पूर्वपदम्",
    padaccheda_dev        = "महान् व्रीहि-अपराह्ण-गृष्टि-इष्वास-जाबाल-भार-भारत-हैलि-हिल-रौरव-प्रवृद्धेषु",
    why_dev               = "(सूत्रम् 6.2.38) महान् व्रीह्यपराह्णगृष्टीष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
