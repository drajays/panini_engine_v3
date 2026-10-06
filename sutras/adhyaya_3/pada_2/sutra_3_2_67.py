"""
3.2.67  जनसनखनक्रमगमो विट्  —  VIDHI

Padaccheda: जन-सन-खन-क्रम-गमः विट्

krt-suffix rule: जनसनखनक्रमगमो विट् (67)
Pāṭha: ashtadhyayi.com data.txt row i=32067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_67_janasanaKa_67"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.67", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janasanaKanakramagamo viw",
    text_dev              = "जनसनखनक्रमगमो विट्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH jana-sana-Kana-krama-gamaH viw kft supi upasarge api Candasi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः जन-सन-खन-क्रम-गमः विट् कृत् सुपि उपसर्गे अपि छन्दसि",
    padaccheda_dev        = "जन-सन-खन-क्रम-गमः विट्",
    why_dev               = "धातोः कृत्-प्रत्ययः [जनसनखनक्रमगमो विट्] विहितः (३.२.67)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
