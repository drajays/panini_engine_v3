"""
4.1.33  पत्युर्नो यज्ञसंयोगे  —  VIDHI

Padaccheda: पत्युः नः यज्ञसंयोगे

पत्युर्नो यज्ञसंयोगे (4.1.33)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_33_patyurno_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_33_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "patyurno yajYasaMyoge",
    text_dev              = "पत्युर्नो यज्ञसंयोगे",
    padaccheda_dev        = "पत्युः नः यज्ञसंयोगे",
    why_dev               = "(सूत्रम् 4.1.33) पत्युर्नो यज्ञसंयोगे।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
