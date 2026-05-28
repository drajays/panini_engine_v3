"""
7.2.44  स्वरतिसूतिसूयतिधूञूदितो वा  —  VIDHI

Padaccheda: स्वरति-सूति-सूयति-धूञ्-ऊदितः वा

स्वरतिसूतिसूयतिधूञूदितो वा (7.2.44)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_44_svaratisUt_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.44", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svaratisUtisUyatiDUYUdito vA",
    text_dev              = "स्वरतिसूतिसूयतिधूञूदितो वा",
    padaccheda_dev        = "स्वरति-सूति-सूयति-धूञ्-ऊदितः वा",
    why_dev               = "(सूत्रम् 7.2.44) स्वरतिसूतिसूयतिधूञूदितो वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
