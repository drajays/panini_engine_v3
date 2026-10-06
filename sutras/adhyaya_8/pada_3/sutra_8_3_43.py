"""
8.3.43  द्विस्त्रिश्चतुरिति कृत्वोऽर्थे  —  VIDHI

Padaccheda: द्विस् · त्रिस् · चतुस् · इति · कृत्वोऽर्थे

द्विस्त्रिश्चतुरिति कृत्वोऽर्थे (8.3.43)
Pāṭha: ashtadhyayi.com data.txt row i=83043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_43_dvistriSca_43"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.43", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'dvistriScaturiti kftvorTe',
    text_dev              = 'द्विस्त्रिश्चतुरिति कृत्वोऽर्थे',
    samagra_slp1          = "kftvaH-arTe dvis-tris-catuH iRaH visarjanIyasya kupvoH anyatarasyAm saH",
    samagra_dev           = "कृत्वः-अर्थे द्विस्-त्रिस्-चतुः इणः विसर्जनीयस्य कुप्वोः अन्यतरस्याम् सः",
    padaccheda_dev        = "द्विस् · त्रिस् · चतुस् · इति · कृत्वोऽर्थे",
    why_dev               = "(सूत्रम् 8.3.43) द्विस्त्रिश्चतुरिति कृत्वोऽर्थे।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
