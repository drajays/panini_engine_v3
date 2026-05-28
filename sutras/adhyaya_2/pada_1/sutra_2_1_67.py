"""
2.1.67  युवा खलतिपलितवलिनजरतीभिः  —  VIDHI

Padaccheda: युवा खलति-पलित-वलिन-जरतीभिः

yuva with khalati, palita, valina, jarati forms karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_67_yuva_khalati"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("karmadharaya" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yuvA KalatipalitavalinajaratIBiH",
    text_dev              = "युवा खलतिपलितवलिनजरतीभिः",
    padaccheda_dev        = "युवा खलति-पलित-वलिन-जरतीभिः",
    why_dev               = "युवा खलति-पलित-आदिभिः सह कर्मधारयः (२.१.६७)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
