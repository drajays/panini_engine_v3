"""
4.3.140  अनुदात्तादेश्च  —  VIDHI

Padaccheda: अनुदात्त-आदेः च

अनुदात्तादेश्च (4.3.140)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_140_anudAttAde_140"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_140_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttAdeSca",
    text_dev              = "अनुदात्तादेश्च",
    padaccheda_dev        = "अनुदात्त-आदेः च",
    why_dev               = "(सूत्रम् 4.3.140) अनुदात्तादेश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
