"""
8.4.39  क्षुभ्नाऽऽदिषु च  —  VIDHI

Padaccheda: क्षुभ्ना-आदिषु च

क्षुभ्नाऽऽदिषु च (8.4.39)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_39_kzuBnAdi_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_39_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzuBnA''dizu ca",
    text_dev              = "क्षुभ्नाऽऽदिषु च",
    padaccheda_dev        = "क्षुभ्ना-आदिषु च",
    why_dev               = "(सूत्रम् 8.4.39) क्षुभ्नाऽऽदिषु च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
