"""
3.3.12  अण् कर्मणि च  —  VIDHI

Padaccheda: अण् कर्मणि च

krt-suffix rule: अण् कर्मणि च
Pāṭha: ashtadhyayi.com data.txt row i=33012 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_12_aR_12"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.12", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.12"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.12",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aR karmaRi ca",
    text_dev              = "अण् कर्मणि च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH Bavizyati aR karmaRi ca kft kriyAyAm kriyArTAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भविष्यति अण् कर्मणि च कृत् क्रियायाम् क्रियार्थायाम्",
    padaccheda_dev        = "अण् कर्मणि च",
    why_dev               = "धातोः प्रत्ययः (३.3.12)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
