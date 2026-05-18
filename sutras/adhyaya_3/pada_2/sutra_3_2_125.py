"""
3.2.125  सम्बोधने च  —  VIDHI

Padaccheda: सम्बोधने च

krt-suffix rule: सम्बोधने च (125)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_125_samboDane_125"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_125_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.125"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.125",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samboDane ca",
    text_dev              = "सम्बोधने च",
    padaccheda_dev        = "सम्बोधने च",
    why_dev               = "धातोः कृत्-प्रत्ययः [सम्बोधने च] विहितः (३.२.125)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
