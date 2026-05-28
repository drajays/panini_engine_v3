"""
2.4.30  अपथं नपुंसकम्  —  VIDHI

Padaccheda: अपथम् नपुंसकम्

apatha is neuter.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_30_apatha_napumsaka"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(
        "dvandva_samasa" in t.tags or "samasa_member" in t.tags
        for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["samasa_kind"]             = "2.4.30"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.30",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "apaTaM napuMsakam",
    text_dev              = "अपथं नपुंसकम्",
    padaccheda_dev        = "अपथम् नपुंसकम्",
    why_dev               = "अपथम् नपुंसकम् (२.४.३०)।",
    anuvritti_from        = ('2.4.26',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
