"""
6.2.36  आचार्योपसर्जनश्चान्तेवासी  —  VIDHI

Padaccheda: आचार्य-उपसर्जनः च अन्तेवासी

आचार्योपसर्जनश्चान्तेवासी (6.2.36)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_36_AcAryopasa_36"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("6_2_36_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.36"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.36",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AcAryopasarjanaScAntevAsI",
    text_dev              = "आचार्योपसर्जनश्चान्तेवासी",
    padaccheda_dev        = "आचार्य-उपसर्जनः च अन्तेवासी",
    why_dev               = "(सूत्रम् 6.2.36) आचार्योपसर्जनश्चान्तेवासी।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
