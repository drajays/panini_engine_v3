"""
8.1.7  उपर्यध्यधसः सामीप्ये  —  VIDHI

Padaccheda: उपरि-अधि-अधसः सामीप्ये

उपर्यध्यधसः सामीप्ये (8.1.7)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_7_uparyaDyaD_7"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.7", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.7"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.7",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uparyaDyaDasaH sAmIpye",
    text_dev              = "उपर्यध्यधसः सामीप्ये",
    padaccheda_dev        = "उपरि-अधि-अधसः सामीप्ये",
    why_dev               = "(सूत्रम् 8.1.7) उपर्यध्यधसः सामीप्ये।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
