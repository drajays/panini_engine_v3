"""
8.4.67  नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्  —  VIDHI

Padaccheda: नः उदात्त-स्वरित-उदयम् अ-गार्ग्य-काश्यप-गालवानाम्

नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम् (8.4.67)
Pāṭha: ashtadhyayi.com data.txt row i=84067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_67_nodAttasva_67"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.67", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nodAttasvaritodayamagArgyakASyapagAlavAnAm",
    text_dev              = "नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm naH udAtta-svarita-udayam a-gArgya-kASyapa-gAlavAnAm anudAttasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् नः उदात्त-स्वरित-उदयम् अ-गार्ग्य-काश्यप-गालवानाम् अनुदात्तस्य",
    padaccheda_dev        = "नः उदात्त-स्वरित-उदयम् अ-गार्ग्य-काश्यप-गालवानाम्",
    why_dev               = "(सूत्रम् 8.4.67) नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
