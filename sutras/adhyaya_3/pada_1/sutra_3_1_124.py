"""
3.1.124  ऋहलोर्ण्यत्  —  VIDHI

Padaccheda: ऋ-हलोः ण्यत्

Krt suffix rule from dhatu: ऋहलोर्ण्यत् (124)
Pāṭha: ashtadhyayi.com data.txt row i=31124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_124_fhalorRyat_124"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.124", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "fhalorRyat",
    text_dev              = "ऋहलोर्ण्यत्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH f-haloH Ryat kft",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः ऋ-हलोः ण्यत् कृत्",
    padaccheda_dev        = "ऋ-हलोः ण्यत्",
    why_dev               = "धातोः [ऋहलोर्ण्यत्]-प्रत्ययः विहितः (३.१.124)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
