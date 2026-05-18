"""
5.2.38  पुरुषहस्तिभ्यामण् च  —  VIDHI

Padaccheda: पुरुष-हस्तिभ्याम् अण् च

पुरुषहस्तिभ्यामण् च (5.2.38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_38_puruzahast_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_38_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puruzahastiByAmaR ca",
    text_dev              = "पुरुषहस्तिभ्यामण् च",
    padaccheda_dev        = "पुरुष-हस्तिभ्याम् अण् च",
    why_dev               = "(सूत्रम् 5.2.38) पुरुषहस्तिभ्यामण् च।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
