"""
3.1.39  भीह्रीभृहुवां श्लुवच्च  —  VIDHI

Padaccheda: भी-ह्री-भृ-हुवाम् श्लु-वत् च

Krt suffix rule from dhatu: भीह्रीभृहुवां श्लुवच्च (39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_39_BIhrIBfhuvAM_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_39_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BIhrIBfhuvAM Sluvacca",
    text_dev              = "भीह्रीभृहुवां श्लुवच्च",
    padaccheda_dev        = "भी-ह्री-भृ-हुवाम् श्लु-वत् च",
    why_dev               = "धातोः [भीह्रीभृहुवां श्लुवच्च]-प्रत्ययः विहितः (३.१.39)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
