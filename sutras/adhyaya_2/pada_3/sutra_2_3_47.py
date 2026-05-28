"""
2.3.47  सम्बोधने च  —  VIDHI

Padaccheda: सम्बोधने च

Also in sambodha (vocative) context.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_47_sambodhan_ca"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samboDane ca",
    text_dev              = "सम्बोधने च",
    padaccheda_dev        = "सम्बोधने च",
    why_dev               = "सम्बोधने च (२.३.४७)।",
    anuvritti_from        = ('2.3.46',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
