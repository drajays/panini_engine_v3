"""
4.3.129  छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ्ञ्यः  —  VIDHI

Padaccheda: छन्दो-गौक्थिक-याज्ञिक-बह्‍वृच-नटात् ञ्यः

छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ्ञ्यः (4.3.129)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_3_129_CandogOkTi_129"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_3_129_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.129"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.129",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandogOkTikayAjYikabahvfcanawAYYyaH",
    text_dev              = "छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ्ञ्यः",
    padaccheda_dev        = "छन्दो-गौक्थिक-याज्ञिक-बह्‍वृच-नटात् ञ्यः",
    why_dev               = "(सूत्रम् 4.3.129) छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ्ञ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
