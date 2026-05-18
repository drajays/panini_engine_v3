"""
4.2.23  विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः  —  VIDHI

Padaccheda: विभाषा फाल्गुनी-श्रवणा-कार्त्तिकी-चैत्रीभ्यः

विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः (4.2.23)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_23_viBAzA_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_23_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA PAlgunISravaRAkArttikIcEtrIByaH",
    text_dev              = "विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः",
    padaccheda_dev        = "विभाषा फाल्गुनी-श्रवणा-कार्त्तिकी-चैत्रीभ्यः",
    why_dev               = "(सूत्रम् 4.2.23) विभाषा फाल्गुनीश्रवणाकार्त्तिकीचैत्रीभ्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
