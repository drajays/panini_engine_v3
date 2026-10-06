"""
6.2.56  प्रथमोऽचिरोपसम्पत्तौ  —  VIDHI

Padaccheda: प्रथमः अचिरोपसम्पत्तौ

प्रथमोऽचिरोपसम्पत्तौ (6.2.56)
Pāṭha: ashtadhyayi.com data.txt row i=62056 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_56_praTamoci_56"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.56", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'praTamociropasampattO',
    text_dev              = 'प्रथमोऽचिरोपसम्पत्तौ',
    samagra_slp1          = "praTamaH acira-upasampattO prakftyA pUrvapadam anyatarasyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रथमः अचिर-उपसम्पत्तौ प्रकृत्या पूर्वपदम् अन्यतरस्याम्",
    padaccheda_dev        = "प्रथमः अचिरोपसम्पत्तौ",
    why_dev               = "(सूत्रम् 6.2.56) प्रथमोऽचिरोपसम्पत्तौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
