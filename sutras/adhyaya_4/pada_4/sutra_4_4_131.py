"""
4.4.131  वेशोयशआदेर्भगाद्यल्  —  VIDHI

Padaccheda: वेशोयश-आदेः भगात् यल्

वेशोयशआदेर्भगाद्यल् (4.4.131)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_131_veSoyaSaAd_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_131_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "veSoyaSaAderBagAdyal",
    text_dev              = "वेशोयशआदेर्भगाद्यल्",
    padaccheda_dev        = "वेशोयश-आदेः भगात् यल्",
    why_dev               = "(सूत्रम् 4.4.131) वेशोयशआदेर्भगाद्यल्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
