"""
2.2.27  तत्र तेनेदमिति सरूपे  —  VIDHI

Padaccheda: तत्र तेन इदम् इति सरूपे

In sarupya context tatra-tena-idam karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_27_tatra_sarupe"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.2.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tatra tenedamiti sarUpe",
    text_dev              = "तत्र तेनेदमिति सरूपे",
    padaccheda_dev        = "तत्र तेन इदम् इति सरूपे",
    why_dev               = "तत्र तेन इदम् इति सरूपे कर्मधारयः (२.२.२७)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
