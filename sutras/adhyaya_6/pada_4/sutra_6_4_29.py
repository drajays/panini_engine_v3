"""
6.4.29  अवोदैधौद्मप्रश्रथहिमश्रथाः  —  VIDHI

Padaccheda: अवोद-एध-ओद्म-प्रश्रथ-हिमश्रथाः

अवोदैधौद्मप्रश्रथहिमश्रथाः (6.4.29)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_29_avodEDOdma_29"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_29_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.29"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.29",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avodEDOdmapraSraTahimaSraTAH",
    text_dev              = "अवोदैधौद्मप्रश्रथहिमश्रथाः",
    padaccheda_dev        = "अवोद-एध-ओद्म-प्रश्रथ-हिमश्रथाः",
    why_dev               = "(सूत्रम् 6.4.29) अवोदैधौद्मप्रश्रथहिमश्रथाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
