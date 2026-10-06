"""
3.3.11  भाववचनाश्च  —  VIDHI

Padaccheda: भाव-वचनाः च

krt-suffix rule: भाववचनाश्च
Pāṭha: ashtadhyayi.com data.txt row i=33011 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_11_BAvavacanA_11"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.11", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.11"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.11",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BAvavacanASca",
    text_dev              = "भाववचनाश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati BAvavacanAH ca kft kriyAyAm kriyArTAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति भाववचनाः च कृत् क्रियायाम् क्रियार्थायाम्",
    padaccheda_dev        = "भाव-वचनाः च",
    why_dev               = "धातोः प्रत्ययः (३.3.11)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
