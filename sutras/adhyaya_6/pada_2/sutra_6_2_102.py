"""
6.2.102  कुसूलकूपकुम्भशालं बिले  —  VIDHI

Padaccheda: कुसूल-कूप-कुम्भ-शालम् बिले

कुसूलकूपकुम्भशालं बिले (6.2.102)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_102_kusUlakUpa_102"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_102_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.102"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.102",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kusUlakUpakumBaSAlaM bile",
    text_dev              = "कुसूलकूपकुम्भशालं बिले",
    padaccheda_dev        = "कुसूल-कूप-कुम्भ-शालम् बिले",
    why_dev               = "(सूत्रम् 6.2.102) कुसूलकूपकुम्भशालं बिले।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
