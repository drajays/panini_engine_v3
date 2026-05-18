"""
5.2.126  स्वामिन्नैश्वर्ये  —  VIDHI

Padaccheda: स्वामिन् ऐश्वर्ये

स्वामिन्नैश्वर्ये (5.2.126)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_126_svAminnESv_126"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_126_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.126",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svAminnESvarye",
    text_dev              = "स्वामिन्नैश्वर्ये",
    padaccheda_dev        = "स्वामिन् ऐश्वर्ये",
    why_dev               = "(सूत्रम् 5.2.126) स्वामिन्नैश्वर्ये।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
