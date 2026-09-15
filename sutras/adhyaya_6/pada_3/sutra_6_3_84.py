"""
6.3.84  समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु  —  VIDHI

Padaccheda: समानस्य छन्दसि अ-मूर्ध-प्रभृति-उदर्केषु

समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु (6.3.84)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_84_samAnasya_84"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.84", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.84"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.84",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAnasya CandasyamUrDapraBftyudarkezu",
    text_dev              = "समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु",
    padaccheda_dev        = "समानस्य छन्दसि अ-मूर्ध-प्रभृति-उदर्केषु",
    why_dev               = "(सूत्रम् 6.3.84) समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
