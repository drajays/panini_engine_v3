"""
3.3.127  कर्तृकर्मणोश्च भूकृञोः  —  VIDHI

Padaccheda: कर्तृ-कर्मणोः च भू-कृञोः

krt-suffix rule: कर्तृकर्मणोश्च भूकृञोः
Pāṭha: ashtadhyayi.com data.txt row i=33127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_127_kartfkarma_127"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.127", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kartfkarmaRoSca BUkfYoH",
    text_dev              = "कर्तृकर्मणोश्च भूकृञोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH kartf-karmaRoH ca BU-kfYoH kft Izat-dus-suzu Kal kfcCra-akfcCra-arTezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः कर्तृ-कर्मणोः च भू-कृञोः कृत् ईषत्-दुस्-सुषु खल् कृच्छ्र-अकृच्छ्र-अर्थेषु",
    padaccheda_dev        = "कर्तृ-कर्मणोः च भू-कृञोः",
    why_dev               = "धातोः प्रत्ययः (३.3.127)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
