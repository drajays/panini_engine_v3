"""
6.2.133  नाचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः  —  VIDHI

Padaccheda: न आचार्य-राज-ॠत्विक्-सयुक्त-ज्ञाति-आख्येभ्यः

नाचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः (6.2.133)
Pāṭha: ashtadhyayi.com data.txt row i=62133 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_133_nAcAryarAj_133"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.133", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.133"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.133",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nAcAryarAjartviksaMyuktajYAtyAKyeByaH",
    text_dev              = "नाचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः",
    samagra_slp1          = "udAttaH uttarapadAdiH na AcArya-rAja-ftvik-saMyukta-jYAti-AKyeByaH tatpuruze putraH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः उत्तरपदादिः न आचार्य-राज-ऋत्विक्-संयुक्त-ज्ञाति-आख्येभ्यः तत्पुरुषे पुत्रः",
    padaccheda_dev        = "न आचार्य-राज-ॠत्विक्-सयुक्त-ज्ञाति-आख्येभ्यः",
    why_dev               = "(सूत्रम् 6.2.133) नाचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
