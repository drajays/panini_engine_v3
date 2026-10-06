"""
3.2.103  सुयजोर्ङ्वनिप्  —  VIDHI

Padaccheda: सु-यजोः ङ्वनिप्

krt-suffix rule: सुयजोर्ङ्वनिप् (103)
Pāṭha: ashtadhyayi.com data.txt row i=32103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_103_suyajorNva_103"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.103", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suyajorNvanip",
    text_dev              = "सुयजोर्ङ्वनिप्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte suyajoH Nvanip kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते सुयजोः ङ्वनिप् कृत्",
    padaccheda_dev        = "सु-यजोः ङ्वनिप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुयजोर्ङ्वनिप्] विहितः (३.२.103)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
