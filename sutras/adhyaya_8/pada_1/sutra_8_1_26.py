"""
8.1.26  सपूर्वायाः प्रथमाया विभाषा  —  VIDHI

Padaccheda: स-पूर्वायाः प्रथमायाः विभाषा

सपूर्वायाः प्रथमाया विभाषा (8.1.26)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_26_sapUrvAyAH_26"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.26", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.26"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.26",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sapUrvAyAH praTamAyA viBAzA",
    text_dev              = "सपूर्वायाः प्रथमाया विभाषा",
    padaccheda_dev        = "स-पूर्वायाः प्रथमायाः विभाषा",
    why_dev               = "(सूत्रम् 8.1.26) सपूर्वायाः प्रथमाया विभाषा।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
