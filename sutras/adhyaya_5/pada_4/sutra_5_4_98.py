"""
5.4.98  उत्तरमृगपूर्वाच्च सक्थ्नः  —  VIDHI

Padaccheda: उत्तर-मृग-पूर्वात् च सक्थ्‍नः

उत्तरमृगपूर्वाच्च सक्थ्नः (5.4.98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_98_uttaramfga_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_98_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttaramfgapUrvAcca sakTnaH",
    text_dev              = "उत्तरमृगपूर्वाच्च सक्थ्नः",
    padaccheda_dev        = "उत्तर-मृग-पूर्वात् च सक्थ्‍नः",
    why_dev               = "(सूत्रम् 5.4.98) उत्तरमृगपूर्वाच्च सक्थ्नः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
