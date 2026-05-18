"""
3.2.60  त्यदादिषु दृशोऽनालोचने कञ् च  —  VIDHI

Padaccheda: त्यद्-आदिषु दृशः अनालोचने कञ् च

krt-suffix rule: त्यदादिषु दृशोऽनालोचने कञ् च (60)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_60_tyadAdizu_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_60_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tyadAdizu dfSo'nAlocane kaY ca",
    text_dev              = "त्यदादिषु दृशोऽनालोचने कञ् च",
    padaccheda_dev        = "त्यद्-आदिषु दृशः अनालोचने कञ् च",
    why_dev               = "धातोः कृत्-प्रत्ययः [त्यदादिषु दृशोऽनालोचने कञ् च] विहितः (३.२.60)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
