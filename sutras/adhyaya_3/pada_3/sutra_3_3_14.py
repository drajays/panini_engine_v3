"""
3.3.14  लृटः सद् वा  —  VIDHI

Padaccheda: लृटः सत् वा

krt-suffix rule: लृटः सद् वा
Pāṭha: ashtadhyayi.com data.txt row i=33014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_14_lfwaH_14"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.14", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lfwaH sad vA",
    text_dev              = "लृटः सद् वा",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati lfwaH sat vA kft Seze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति लृटः सत् वा कृत् शेषे",
    padaccheda_dev        = "लृटः सत् वा",
    why_dev               = "धातोः प्रत्ययः (३.3.14)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
