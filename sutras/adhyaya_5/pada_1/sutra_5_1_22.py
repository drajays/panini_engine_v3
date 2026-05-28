"""
5.1.22  संख्याया अतिशदन्तायाः कन्  —  VIDHI

Padaccheda: संख्याया अ-ति-शत्-अन्तायाः कन्

संख्याया अतिशदन्तायाः कन् (5.1.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_22_saMKyAyA_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.22", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMKyAyA atiSadantAyAH kan",
    text_dev              = "संख्याया अतिशदन्तायाः कन्",
    padaccheda_dev        = "संख्याया अ-ति-शत्-अन्तायाः कन्",
    why_dev               = "(सूत्रम् 5.1.22) संख्याया अतिशदन्तायाः कन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
