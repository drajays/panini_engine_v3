"""
3.3.137  कालविभागे चानहोरात्राणाम्  —  VIDHI

Padaccheda: काल-विभागे च अनहोरात्राणाम्

krt-suffix rule: कालविभागे चानहोरात्राणाम्
Pāṭha: ashtadhyayi.com data.txt row i=33137 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_137_kAlaviBAge_137"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.137", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAlaviBAge cAnahorAtrARAm",
    text_dev              = "कालविभागे चानहोरात्राणाम्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kAlaviBAge ca anahorAtrARAm kft na anadyatanavat a-varasmin maryAdAvacane Bavizyati",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कालविभागे च अनहोरात्राणाम् कृत् न अनद्यतनवत् अ-वरस्मिन् मर्यादावचने भविष्यति",
    padaccheda_dev        = "काल-विभागे च अनहोरात्राणाम्",
    why_dev               = "धातोः प्रत्ययः (३.3.137)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
