"""
8.3.110  न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्  —  VIDHI

Padaccheda: न र-पर-सृपि-सृजि-स्पृशि-स्पृहि-सवन-आदीनाम्

न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम् (8.3.110)
Pāṭha: ashtadhyayi.com data.txt row i=83110 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_110_na_110"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.110", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.110"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.110",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na raparasfpisfjispfSispfhisavanAdInAm",
    text_dev              = "न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH na rapara-sfpi-sfji-spfSi-spfhi-savanAdInAm saH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः न रपर-सृपि-सृजि-स्पृशि-स्पृहि-सवनादीनाम् सः",
    padaccheda_dev        = "न र-पर-सृपि-सृजि-स्पृशि-स्पृहि-सवन-आदीनाम्",
    why_dev               = "(सूत्रम् 8.3.110) न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
