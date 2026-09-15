"""
6.4.175  ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि  —  VIDHI

Padaccheda: ऋत्व्य-वास्त्व्य-वास्त्व-माध्वी-हिरण्ययानि छन्दसि

ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि (6.4.175)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_175_ftvyavAstv_175"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.175", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.175"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.175",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ftvyavAstvyavAstvamADvIhiraRyayAni cCandasi",
    text_dev              = "ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि",
    padaccheda_dev        = "ऋत्व्य-वास्त्व्य-वास्त्व-माध्वी-हिरण्ययानि छन्दसि",
    why_dev               = "(सूत्रम् 6.4.175) ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि च्छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
