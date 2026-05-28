"""
3.3.146  किंकिलास्त्यर्थेषु लृट्  —  VIDHI

Padaccheda: किंकिल-अस्त्यर्थेषु लृट्

krt-suffix rule: किंकिलास्त्यर्थेषु लृट्
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_3_146_kiMkilAsty_146"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("dhatu" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("3_3_146_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.146"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.146",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kiMkilAstyarTezu lfw",
    text_dev              = "किंकिलास्त्यर्थेषु लृट्",
    padaccheda_dev        = "किंकिल-अस्त्यर्थेषु लृट्",
    why_dev               = "धातोः प्रत्ययः (३.3.146)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
