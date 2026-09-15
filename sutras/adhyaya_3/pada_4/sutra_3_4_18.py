"""
3.4.18  अलङ्खल्वोः प्रतिषेधयोः प्राचां क्त्वा  —  VIDHI

Padaccheda: अलं-खल्वोः प्रतिषेधयोः प्राचाम् क्त्वा

krt-suffix rule: अलङ्खल्वोः प्रतिषेधयोः प्राचां क्त्वा
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_18_alaNKalvoH_18"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.18", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "alaNKalvoH pratizeDayoH prAcAM ktvA",
    text_dev              = "अलङ्खल्वोः प्रतिषेधयोः प्राचां क्त्वा",
    padaccheda_dev        = "अलं-खल्वोः प्रतिषेधयोः प्राचाम् क्त्वा",
    why_dev               = "धातोः प्रत्ययः (३.4.18)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
