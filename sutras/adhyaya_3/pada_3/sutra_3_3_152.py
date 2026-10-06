"""
3.3.152  उताप्योः समर्थयोर्लिङ्  —  VIDHI

Padaccheda: उत-अप्योः समर्थयोः लिङ्

krt-suffix rule: उताप्योः समर्थयोर्लिङ्
Pāṭha: ashtadhyayi.com data.txt row i=33152 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_152_utApyoH_152"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.152", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.152"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.152",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "utApyoH samarTayorliN",
    text_dev              = "उताप्योः समर्थयोर्लिङ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH uta-apyoH samarTayoH liN kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः उत-अप्योः समर्थयोः लिङ् कृत्",
    padaccheda_dev        = "उत-अप्योः समर्थयोः लिङ्",
    why_dev               = "धातोः प्रत्ययः (३.3.152)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
