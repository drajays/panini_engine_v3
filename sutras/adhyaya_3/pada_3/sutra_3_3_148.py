"""
3.3.148  यच्चयत्रयोः  —  VIDHI

Padaccheda: यच्च-यत्रयोः

krt-suffix rule: यच्चयत्रयोः
Pāṭha: ashtadhyayi.com data.txt row i=33148 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_148_yaccayatra_148"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.148", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.148"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.148",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yaccayatrayoH",
    text_dev              = "यच्चयत्रयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH yacca-yatrayoH kft utApyoH anavakxpti-amarzayoH liN",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः यच्च-यत्रयोः कृत् उताप्योः अनवकॢप्ति-अमर्षयोः लिङ्",
    padaccheda_dev        = "यच्च-यत्रयोः",
    why_dev               = "धातोः प्रत्ययः (३.3.148)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
