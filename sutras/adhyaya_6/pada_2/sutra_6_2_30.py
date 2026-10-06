"""
6.2.30  बह्वन्यतरस्याम्  —  VIDHI

Padaccheda: बहु अन्यतरस्याम्

बह्वन्यतरस्याम् (6.2.30)
Pāṭha: ashtadhyayi.com data.txt row i=62030 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_30_bahvanyata_30"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.30", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahvanyatarasyAm",
    text_dev              = "बह्वन्यतरस्याम्",
    samagra_slp1          = "bahu anyatarasyAm pUrvapadam prakftyA iganta-kAla-kapAla-BagAla-SarAvezu dvigO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "बहु अन्यतरस्याम् पूर्वपदम् प्रकृत्या इगन्त-काल-कपाल-भगाल-शरावेषु द्विगौ",
    padaccheda_dev        = "बहु अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.2.30) बह्वन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
