"""
6.3.10  कारनाम्नि च प्राचां हलादौ  —  VIDHI

Padaccheda: कारनाम्नि च प्राचाम् हल्-आदौ

कारनाम्नि च प्राचां हलादौ (6.3.10)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_10_kAranAmni_10"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.10", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.10"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.10",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAranAmni ca prAcAM halAdO",
    text_dev              = "कारनाम्नि च प्राचां हलादौ",
    padaccheda_dev        = "कारनाम्नि च प्राचाम् हल्-आदौ",
    why_dev               = "(सूत्रम् 6.3.10) कारनाम्नि च प्राचां हलादौ।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
