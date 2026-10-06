"""
3.2.31  उदि कूले रुजिवहोः  —  VIDHI

Padaccheda: उदि कूले रुजि-वहोः

krt-suffix rule: उदि कूले रुजिवहोः (31)
Pāṭha: ashtadhyayi.com data.txt row i=32031 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_31_udi_31"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.2.31", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udi kUle rujivahoH",
    text_dev              = "उदि कूले रुजिवहोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH udi kUle ruji-vahoH kft karmaRi anupasarge supi KaS",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः उदि कूले रुजि-वहोः कृत् कर्मणि अनुपसर्गे सुपि खश्",
    padaccheda_dev        = "उदि कूले रुजि-वहोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [उदि कूले रुजिवहोः] विहितः (३.२.31)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
