"""
4.1.164  भ्रातरि च ज्यायसि  —  VIDHI

Padaccheda: भ्रातरि च ज्यायसि

भ्रातरि च ज्यायसि (4.1.164)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_164_BrAtari_164"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_164_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BrAtari ca jyAyasi",
    text_dev              = "भ्रातरि च ज्यायसि",
    padaccheda_dev        = "भ्रातरि च ज्यायसि",
    why_dev               = "(सूत्रम् 4.1.164) भ्रातरि च ज्यायसि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
