"""
8.3.77  वेः स्कभ्नातेर्नित्यम्  —  VIDHI

Padaccheda: वेः स्कभ्नातेः नित्यम्

वेः स्कभ्नातेर्नित्यम् (8.3.77)
Pāṭha: ashtadhyayi.com data.txt row i=83077 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_77_veH_77"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.77", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "veH skaBnAternityam",
    text_dev              = "वेः स्कभ्नातेर्नित्यम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH veH skaBnAteH nityam saH upasargAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः वेः स्कभ्नातेः नित्यम् सः उपसर्गात्",
    padaccheda_dev        = "वेः स्कभ्नातेः नित्यम्",
    why_dev               = "(सूत्रम् 8.3.77) वेः स्कभ्नातेर्नित्यम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
