"""
2.4.17  स नपुंसकम्  —  VIDHI

Padaccheda: सः नपुंसकम्

The dvandva compound is neuter.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_17_sa_napumsaka"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sa napuMsakam",
    text_dev              = "स नपुंसकम्",
    padaccheda_dev        = "सः नपुंसकम्",
    why_dev               = "सः नपुंसकम् (२.४.१७)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
