"""
4.1.50  क्रीतात् करणपूर्वात्  —  VIDHI

Padaccheda: क्रीतात् करण-पूर्वात्

क्रीतात् करणपूर्वात् (4.1.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_50_krItAt_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "krItAt karaRapUrvAt",
    text_dev              = "क्रीतात् करणपूर्वात्",
    padaccheda_dev        = "क्रीतात् करण-पूर्वात्",
    why_dev               = "(सूत्रम् 4.1.50) क्रीतात् करणपूर्वात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
