"""
3.1.31  आयादय आर्धधातुके वा  —  VIDHI

Padaccheda: आय्-आदयः आर्धधातुके वा

Krt suffix rule from dhatu: आयादय आर्धद्धातुके वा (31)
Pāṭha: ashtadhyayi.com data.txt row i=31031 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_31_AyAdaya_31"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.31", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'AyAdaya ArDaDAtuke vA',
    text_dev              = 'आयादय आर्धधातुके वा',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH AyAdayaH ArDaDAtuke vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः आयादयः आर्धधातुके वा",
    padaccheda_dev        = "आय्-आदयः आर्धधातुके वा",
    why_dev               = "धातोः [आयादय आर्धद्धातुके वा]-प्रत्ययः विहितः (३.१.31)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
