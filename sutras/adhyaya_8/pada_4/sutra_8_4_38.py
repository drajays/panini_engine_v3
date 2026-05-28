"""
8.4.38  पदव्यवायेऽपि  —  VIDHI

Padaccheda: पद-व्यवाये अपि

पदव्यवायेऽपि (8.4.38)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_38_padavyavAy_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "padavyavAye'pi",
    text_dev              = "पदव्यवायेऽपि",
    padaccheda_dev        = "पद-व्यवाये अपि",
    why_dev               = "(सूत्रम् 8.4.38) पदव्यवायेऽपि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
