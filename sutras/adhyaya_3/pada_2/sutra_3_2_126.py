"""
3.2.126  लक्षणहेत्वोः क्रियायाः  —  VIDHI

Padaccheda: लक्षण-हेत्वोः क्रियायाः

krt-suffix rule: लक्षणहेत्वोः क्रियायाः (126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_126_lakzaRahet_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_126_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lakzaRahetvoH kriyAyAH",
    text_dev              = "लक्षणहेत्वोः क्रियायाः",
    padaccheda_dev        = "लक्षण-हेत्वोः क्रियायाः",
    why_dev               = "धातोः कृत्-प्रत्ययः [लक्षणहेत्वोः क्रियायाः] विहितः (३.२.126)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
