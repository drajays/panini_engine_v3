"""
6.1.95  ओमाङोश्च  —  VIDHI

Padaccheda: ओम्-आङोः च

ओमाङोश्च (6.1.95)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_95_omANgoSca_95"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.95", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.95"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.95",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "omANgoSca",
    text_dev              = "ओमाङोश्च",
    padaccheda_dev        = "ओम्-आङोः च",
    why_dev               = "(सूत्रम् 6.1.95) ओमाङोश्च।",
    apavada_of     = ("6.1.88",),   # अपवाद of 6.1.88 — sutra_ref_out resolver.apavada_of
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
