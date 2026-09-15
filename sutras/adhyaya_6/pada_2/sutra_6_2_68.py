"""
6.2.68  पापं च शिल्पिनि  —  VIDHI

Padaccheda: पापम् च शिल्पिनि

पापं च शिल्पिनि (6.2.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_68_pApaM_68"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.68", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pApaM ca Silpini",
    text_dev              = "पापं च शिल्पिनि",
    padaccheda_dev        = "पापम् च शिल्पिनि",
    why_dev               = "(सूत्रम् 6.2.68) पापं च शिल्पिनि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
