"""
3.3.159  लिङ् च  —  VIDHI

Padaccheda: लिङ् च

krt-suffix rule: लिङ् च
Pāṭha: ashtadhyayi.com data.txt row i=33159 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_159_liN_159"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.159", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.159"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.159",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "liN ca",
    text_dev              = "लिङ् च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH liN ca kft icCArTezu samAnakartfkezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः लिङ् च कृत् इच्छार्थेषु समानकर्तृकेषु",
    padaccheda_dev        = "लिङ् च",
    why_dev               = "धातोः प्रत्ययः (३.3.159)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
