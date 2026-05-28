"""
8.2.103  स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु  —  VIDHI

Padaccheda: स्वरितम् आम्रेडिते असूया-सम्मति-कोप-कुत्सनेषु

स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु (8.2.103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_103_svaritamAm_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_103_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "svaritamAmreqite'sUyAsammatikopakutsanezu",
    text_dev              = "स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु",
    padaccheda_dev        = "स्वरितम् आम्रेडिते असूया-सम्मति-कोप-कुत्सनेषु",
    why_dev               = "(सूत्रम् 8.2.103) स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
