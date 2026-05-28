"""
5.3.83  ठाजादावूर्ध्वं द्वितीयादचः  —  VIDHI

Padaccheda: ठ-अच्-आदौ ऊर्ध्वम् द्वितीयात् अचः

ठाजादावूर्ध्वं द्वितीयादचः (5.3.83)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_3_83_WAjAdAvUrD_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.3.83", state, "5.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.3.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.3.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "WAjAdAvUrDvaM dvitIyAdacaH",
    text_dev              = "ठाजादावूर्ध्वं द्वितीयादचः",
    padaccheda_dev        = "ठ-अच्-आदौ ऊर्ध्वम् द्वितीयात् अचः",
    why_dev               = "(सूत्रम् 5.3.83) ठाजादावूर्ध्वं द्वितीयादचः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
