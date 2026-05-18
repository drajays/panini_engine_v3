"""
6.4.25  दन्शसञ्जस्वञ्जां शपि  —  VIDHI

Padaccheda: दंश-सञ्ज-स्वञ्जाम् शपि

दन्शसञ्जस्वञ्जां शपि (6.4.25)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_4_25_danSasaYja_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_4_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "danSasaYjasvaYjAM Sapi",
    text_dev              = "दन्शसञ्जस्वञ्जां शपि",
    padaccheda_dev        = "दंश-सञ्ज-स्वञ्जाम् शपि",
    why_dev               = "(सूत्रम् 6.4.25) दन्शसञ्जस्वञ्जां शपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
