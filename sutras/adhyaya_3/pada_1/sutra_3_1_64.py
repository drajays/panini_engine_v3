"""
3.1.64  न रुधः  —  VIDHI

Padaccheda: न रुधः

Krt suffix rule from dhatu: न रुधः (64)
Pāṭha: ashtadhyayi.com data.txt row i=31064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_64_na_64"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.64", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.64",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na ruDaH",
    text_dev              = "न रुधः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH na ruDaH luNi cleH ciR te karmakartari",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः न रुधः लुङि च्लेः चिण् ते कर्मकर्तरि",
    padaccheda_dev        = "न रुधः",
    why_dev               = "धातोः [न रुधः]-प्रत्ययः विहितः (३.१.64)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
