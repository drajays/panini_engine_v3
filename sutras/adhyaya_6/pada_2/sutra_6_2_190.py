"""
6.2.190  पुरुषश्चान्वादिष्टः  —  VIDHI

Padaccheda: पुरुषः च अन्वादिष्टः

पुरुषश्चान्वादिष्टः (6.2.190)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_190_puruzaScAn_190"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.190", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.190"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.190",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puruzaScAnvAdizwaH",
    text_dev              = "पुरुषश्चान्वादिष्टः",
    padaccheda_dev        = "पुरुषः च अन्वादिष्टः",
    why_dev               = "(सूत्रम् 6.2.190) पुरुषश्चान्वादिष्टः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
