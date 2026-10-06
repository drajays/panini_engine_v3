"""
3.2.132  सुञो यज्ञसंयोगे  —  VIDHI

Padaccheda: सुञः यज्ञ-संयोगे

krt-suffix rule: सुञो यज्ञसंयोगे (132)
Pāṭha: ashtadhyayi.com data.txt row i=32132 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_132_suYo_132"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.132", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.132"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suYo yajYasaMyoge",
    text_dev              = "सुञो यज्ञसंयोगे",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne suYaH yajYasaMyoge kft Satf",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने सुञः यज्ञसंयोगे कृत् शतृ",
    padaccheda_dev        = "सुञः यज्ञ-संयोगे",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुञो यज्ञसंयोगे] विहितः (३.२.132)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
