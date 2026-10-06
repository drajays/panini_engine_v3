"""
3.3.60  नौ ण च  —  VIDHI

Padaccheda: नौ ण (लुप्तप्रथमान्तनिर्देशः) च

krt-suffix rule: नौ ण च
Pāṭha: ashtadhyayi.com data.txt row i=33060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_60_nO_60"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.60", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nO Ra ca",
    text_dev              = "नौ ण च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm nO Ra ca kft ap adaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् नौ ण च कृत् अप् अदः",
    padaccheda_dev        = "नौ ण (लुप्तप्रथमान्तनिर्देशः) च",
    why_dev               = "धातोः प्रत्ययः (३.3.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
