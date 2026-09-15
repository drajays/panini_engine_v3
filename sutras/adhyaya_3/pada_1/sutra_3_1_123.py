"""
3.1.123  छन्दसि निष्टर्क्यदेवहूयप्रणीयोन्नीयोच्छिष्य  —  VIDHI

Padaccheda: छन्दसि निष्टर्क्य-देवहूय-प्रणीय-उन्नीय-उच्छिष्य-मर्य-स्तर्या-ध्वर्य-खन्य-खान्य-देवयज्या-आपृच्छ्य-प्रतिषीव्य-ब्रह्मवाद्य-भाव्य-स्ताव्य-उपचाय्यपृडानि

Krt suffix rule from dhatu: छन्दसि निष्टर्क्यदेवहूयप्रणीयोन्नीयोच्छिष्य (123)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_1_123_Candasi_123"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.1.123", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.123"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.123",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasi nizwarkyadevahUyapraRIyonnIyocCizya",
    text_dev              = "छन्दसि निष्टर्क्यदेवहूयप्रणीयोन्नीयोच्छिष्य",
    padaccheda_dev        = "छन्दसि निष्टर्क्य-देवहूय-प्रणीय-उन्नीय-उच्छिष्य-मर्य-स्तर्या-ध्वर्य-खन्य-खान्य-देवयज्या-आपृच्छ्य-प्रतिषीव्य-ब्रह्मवाद्य-भाव्य-स्ताव्य-उपचाय्यपृडानि",
    why_dev               = "धातोः [छन्दसि निष्टर्क्यदेवहूयप्रणीयोन्नीयोच्छिष्य]-प्रत्ययः विहितः (३.१.123)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
