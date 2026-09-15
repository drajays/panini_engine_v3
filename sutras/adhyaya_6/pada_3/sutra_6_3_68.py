"""
6.3.68  इच एकाचोऽम्प्रत्ययवच्च  —  VIDHI

Padaccheda: इचः एक-अचः अम् प्रत्यय-वत् च

इच एकाचोऽम्प्रत्ययवच्च (6.3.68)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_68_ica_68"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.68", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ica ekAco'mpratyayavacca",
    text_dev              = "इच एकाचोऽम्प्रत्ययवच्च",
    padaccheda_dev        = "इचः एक-अचः अम् प्रत्यय-वत् च",
    why_dev               = "(सूत्रम् 6.3.68) इच एकाचोऽम्प्रत्ययवच्च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
