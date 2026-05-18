"""
5.4.78  ब्रह्महस्तिभ्याम् वर्च्चसः  —  VIDHI

Padaccheda: ब्रह्म-हस्तिभ्याम् वर्च्चसः

ब्रह्महस्तिभ्याम् वर्च्चसः (5.4.78)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_4_78_brahmahast_78"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_4_78_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.78"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "brahmahastiByAm varccasaH",
    text_dev              = "ब्रह्महस्तिभ्याम् वर्च्चसः",
    padaccheda_dev        = "ब्रह्म-हस्तिभ्याम् वर्च्चसः",
    why_dev               = "(सूत्रम् 5.4.78) ब्रह्महस्तिभ्याम् वर्च्चसः।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
