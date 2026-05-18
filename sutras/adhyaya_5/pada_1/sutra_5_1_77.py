"""
5.1.77  उत्तरपथेनाहृतं च  —  VIDHI

Padaccheda: उत्तरपथेन आहृतम् च

उत्तरपथेनाहृतं च (5.1.77)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_77_uttarapaTe_77"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_77_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.77"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.77",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttarapaTenAhftaM ca",
    text_dev              = "उत्तरपथेनाहृतं च",
    padaccheda_dev        = "उत्तरपथेन आहृतम् च",
    why_dev               = "(सूत्रम् 5.1.77) उत्तरपथेनाहृतं च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
