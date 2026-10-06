"""
3.1.60  चिण् ते पदः  —  VIDHI

Padaccheda: चिण् ते पदः

Krt suffix rule from dhatu: चिण् ते पदः (60)
Pāṭha: ashtadhyayi.com data.txt row i=31060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_60_ciR_60"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.60", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ciR te padaH",
    text_dev              = "चिण् ते पदः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH ciR te padaH luNi cleH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः चिण् ते पदः लुङि च्लेः",
    padaccheda_dev        = "चिण् ते पदः",
    why_dev               = "धातोः [चिण् ते पदः]-प्रत्ययः विहितः (३.१.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
