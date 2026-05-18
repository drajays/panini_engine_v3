"""
4.2.15  स्थण्डिलाच्छयितरि व्रते  —  VIDHI

Padaccheda: स्थण्डिलात् शयितरि व्रते

स्थण्डिलाच्छयितरि व्रते (4.2.15)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_15_sTaRqilAcC_15"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_15_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.15"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.15",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sTaRqilAcCayitari vrate",
    text_dev              = "स्थण्डिलाच्छयितरि व्रते",
    padaccheda_dev        = "स्थण्डिलात् शयितरि व्रते",
    why_dev               = "(सूत्रम् 4.2.15) स्थण्डिलाच्छयितरि व्रते।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
