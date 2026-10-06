"""
8.3.71  सिवादीनां वाऽड्व्यवायेऽपि  —  VIDHI

Padaccheda: सिव-आदीनाम् वा अट्-अव्यवाये अपि

सिवादीनां वाऽड्व्यवायेऽपि (8.3.71)
Pāṭha: ashtadhyayi.com data.txt row i=83071 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_71_sivAdInAM_71"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.71", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.71"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.71",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'sivAdInAM vAqvyavAyepi',
    text_dev              = 'सिवादीनां वाऽड्व्यवायेऽपि',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH sivAdInAm vA aqvyavAye api saH upasargAt pariniviByaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः सिवादीनाम् वा अड्व्यवाये अपि सः उपसर्गात् परिनिविभ्यः",
    padaccheda_dev        = "सिव-आदीनाम् वा अट्-अव्यवाये अपि",
    why_dev               = "(सूत्रम् 8.3.71) सिवादीनां वाऽड्व्यवायेऽपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
