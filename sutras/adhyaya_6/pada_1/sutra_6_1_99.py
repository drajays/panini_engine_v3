"""
6.1.99  नाम्रेडितस्यान्त्यस्य तु वा  —  VIDHI

Padaccheda: न आम्रेडितस्य अन्त्यस्य तु वा

नाम्रेडितस्यान्त्यस्य तु वा (6.1.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_99_nAmreQitas_99"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.99", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAmreQitasyAntyasya tu vA",
    text_dev              = "नाम्रेडितस्यान्त्यस्य तु वा",
    padaccheda_dev        = "न आम्रेडितस्य अन्त्यस्य तु वा",
    why_dev               = "(सूत्रम् 6.1.99) नाम्रेडितस्यान्त्यस्य तु वा।",
    apavada_of     = ("6.1.98",),   # अपवाद of 6.1.98 — sutra_ref_out resolver.apavada_of
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
