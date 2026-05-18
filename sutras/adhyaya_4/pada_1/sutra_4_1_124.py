"""
4.1.124  विकर्णकुषीतकात् काश्यपे  —  VIDHI

Padaccheda: विकर्ण-कुषीतकात् काश्यपे

विकर्णकुषीतकात् काश्यपे (4.1.124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_124_vikarRakuz_124"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_124_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vikarRakuzItakAt kASyape",
    text_dev              = "विकर्णकुषीतकात् काश्यपे",
    padaccheda_dev        = "विकर्ण-कुषीतकात् काश्यपे",
    why_dev               = "(सूत्रम् 4.1.124) विकर्णकुषीतकात् काश्यपे।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
