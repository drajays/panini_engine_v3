"""
3.3.65  क्वणो वीणायां च  —  VIDHI

Padaccheda: क्वणः वीणायाम् च

krt-suffix rule: क्वणो वीणायां च
Pāṭha: ashtadhyayi.com data.txt row i=33065 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_65_kvaRo_65"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.65", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kvaRo vIRAyAM ca",
    text_dev              = "क्वणो वीणायां च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm kvaRaH vIRAyAm ca kft ap anupasarge vA nO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् क्वणः वीणायाम् च कृत् अप् अनुपसर्गे वा नौ",
    padaccheda_dev        = "क्वणः वीणायाम् च",
    why_dev               = "धातोः प्रत्ययः (३.3.65)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
