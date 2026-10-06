"""
3.1.104  उपसर्या काल्या प्रजने  —  VIDHI

Padaccheda: उपसर्या काल्या प्रजने

Krt suffix rule from dhatu: उपसर्या काल्या प्रजने (104)
Pāṭha: ashtadhyayi.com data.txt row i=31104 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_104_upasaryA_104"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.104", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.104"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.104",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasaryA kAlyA prajane",
    text_dev              = "उपसर्या काल्या प्रजने",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca kftyAH DAtoH upasaryA kAlyA prajane kft yat anupasarge",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च कृत्याः धातोः उपसर्या काल्या प्रजने कृत् यत् अनुपसर्गे",
    padaccheda_dev        = "उपसर्या काल्या प्रजने",
    why_dev               = "धातोः [उपसर्या काल्या प्रजने]-प्रत्ययः विहितः (३.१.104)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
