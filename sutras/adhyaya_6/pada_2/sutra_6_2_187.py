"""
6.2.187  स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च  —  VIDHI

Padaccheda: स्फिग-पूत-वीणा-अञ्जः-अध्व-कुक्षि-सीरनाम-नाम च

स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च (6.2.187)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_187_sPigapUtav_187"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.187"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.187",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sPigapUtavIRA'Yjo'DvakukzisIranAmanAma ca",
    text_dev              = "स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च",
    padaccheda_dev        = "स्फिग-पूत-वीणा-अञ्जः-अध्व-कुक्षि-सीरनाम-नाम च",
    why_dev               = "(सूत्रम् 6.2.187) स्फिगपूतवीणाऽञ्जोऽध्वकुक्षिसीरनामनाम च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
