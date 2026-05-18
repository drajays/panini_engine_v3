"""
2.1.66  प्रशंसावचनैश्च  —  VIDHI

Padaccheda: प्रशंसा-वचनैः च

Praise words (prashamsa-vacana) form karmadharaya compound.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_66_prasansa_vacana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_66_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "praSaMsAvacanESca",
    text_dev              = "प्रशंसावचनैश्च",
    padaccheda_dev        = "प्रशंसा-वचनैः च",
    why_dev               = "प्रशंसा-वचनैश्च कर्मधारयः (२.१.६६)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
