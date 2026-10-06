"""
3.2.69  क्रव्ये च  —  VIDHI

Padaccheda: क्रव्ये च

krt-suffix rule: क्रव्ये च (69)
Pāṭha: ashtadhyayi.com data.txt row i=32069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_69_kravye_69"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.69", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kravye ca",
    text_dev              = "क्रव्ये च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kravye ca kft supi api upasarge viw adaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः क्रव्ये च कृत् सुपि अपि उपसर्गे विट् अदः",
    padaccheda_dev        = "क्रव्ये च",
    why_dev               = "धातोः कृत्-प्रत्ययः [क्रव्ये च] विहितः (३.२.69)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
