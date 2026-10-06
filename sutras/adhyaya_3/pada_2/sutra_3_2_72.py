"""
3.2.72  अवे यजः  —  VIDHI

Padaccheda: अवे यजः

krt-suffix rule: अवे यजः (72)
Pāṭha: ashtadhyayi.com data.txt row i=32072 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_72_ave_72"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.72", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.72"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.72",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ave yajaH",
    text_dev              = "अवे यजः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH ave yajaH kft supi api upasarge mantre Rvin",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः अवे यजः कृत् सुपि अपि उपसर्गे मन्त्रे ण्विन्",
    padaccheda_dev        = "अवे यजः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अवे यजः] विहितः (३.२.72)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
