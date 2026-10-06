"""
3.3.36  समि मुष्टौ  —  VIDHI

Padaccheda: समि मुष्टौ

krt-suffix rule: समि मुष्टौ
Pāṭha: ashtadhyayi.com data.txt row i=33036 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_36_sami_36"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.36", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sami muzwO",
    text_dev              = "समि मुष्टौ",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm sami muzwO kft GaY grahaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् समि मुष्टौ कृत् घञ् ग्रहः",
    padaccheda_dev        = "समि मुष्टौ",
    why_dev               = "धातोः प्रत्ययः (३.3.36)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
