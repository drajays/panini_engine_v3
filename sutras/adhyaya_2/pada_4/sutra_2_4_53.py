"""
2.4.53  ब्रुवो वचिः  —  VIDHI

Padaccheda: ब्रुवः वचिः

bruv root is replaced by vac.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_53_bruva_vaci"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_4_53_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bruvo vaciH",
    text_dev              = "ब्रुवो वचिः",
    padaccheda_dev        = "ब्रुवः वचिः",
    why_dev               = "ब्रुवः वचिः (२.४.५३)।",
    anuvritti_from        = ('2.4.40',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
