"""
2.3.40  आयुक्तकुशलाभ्यां चासेवायाम्  —  VIDHI

Padaccheda: आयुक्त-कुशलाभ्याम् च आसेवायाम्

ayukta and kusala also in service context take sasthi.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_40_ayukta_kusala"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.40",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AyuktakuSalAByAM cAsevAyAm",
    text_dev              = "आयुक्तकुशलाभ्यां चासेवायाम्",
    padaccheda_dev        = "आयुक्त-कुशलाभ्याम् च आसेवायाम्",
    why_dev               = "आयुक्त-कुशलाभ्याम् च आसेवायाम् (२.३.४०)।",
    anuvritti_from        = ('2.3.39',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
