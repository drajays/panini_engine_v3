"""
6.4.157  प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः  —  VIDHI

Padaccheda: प्रिय-स्थिर-स्फिर-उरु-बहुल-गुरु-वृद्ध-तृप्र-दीर्घ-वृन्दारकाणाम् प्र-स्थ-वर्-बंहि-गर्-वर्षि-त्रप्-द्राघि-वृन्दाः

प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः (6.4.157)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "6_4_157_priyasTira_157"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("6.4.157", state, "6.4.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.157"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.157",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "priyasTirasPirorubahulaguruvfdDatfpradIrGavfndArakARAM prasTasPavarbaMhigarvarzitrabdrAGivfndAH",
    text_dev              = "प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः",
    padaccheda_dev        = "प्रिय-स्थिर-स्फिर-उरु-बहुल-गुरु-वृद्ध-तृप्र-दीर्घ-वृन्दारकाणाम् प्र-स्थ-वर्-बंहि-गर्-वर्षि-त्रप्-द्राघि-वृन्दाः",
    why_dev               = "(सूत्रम् 6.4.157) प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
