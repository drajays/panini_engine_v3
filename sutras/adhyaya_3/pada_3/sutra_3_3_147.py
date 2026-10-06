"""
3.3.147  जातुयदोर्लिङ्  —  VIDHI

Padaccheda: जातु-यदोः लिङ्

krt-suffix rule: जातुयदोर्लिङ्
Pāṭha: ashtadhyayi.com data.txt row i=33147 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_147_jAtuyadorl_147"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.147", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.147"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.147",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jAtuyadorliN",
    text_dev              = "जातुयदोर्लिङ्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH jAtu-yadoH liN kft utApyoH anavakxpti-amarzayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः जातु-यदोः लिङ् कृत् उताप्योः अनवकॢप्ति-अमर्षयोः",
    padaccheda_dev        = "जातु-यदोः लिङ्",
    why_dev               = "धातोः प्रत्ययः (३.3.147)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
