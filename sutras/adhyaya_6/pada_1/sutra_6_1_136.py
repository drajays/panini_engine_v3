"""
6.1.136  अडभ्यासव्यवायेऽपि  —  VIDHI

Padaccheda: अट्-अभ्यास-व्यवाये अपि

अडभ्यासव्यवायेऽपि (6.1.136)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_136_aqaByAsavy_136"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.136"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.136",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aqaByAsavyavAye'pi",
    text_dev              = "अडभ्यासव्यवायेऽपि",
    padaccheda_dev        = "अट्-अभ्यास-व्यवाये अपि",
    why_dev               = "(सूत्रम् 6.1.136) अडभ्यासव्यवायेऽपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
