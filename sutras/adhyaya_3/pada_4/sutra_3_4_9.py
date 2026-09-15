"""
3.4.9  तुमर्थे सेसेनसेअसेन्क्सेकसेनध्यैअध्यैन्कध्यैकध्यैन्शध्यैशध्यैन्तवैतवेङ्तवेनः  —  VIDHI

Padaccheda: तुमर्थे से-सेन्-असे-असेन्-क्से-कसेन्-अध्यै-अध्यैन्-कध्यै-कध्यैन्-शध्यै-शध्यैन्-तवै-तवेङ्-तवेनः

krt-suffix rule: तुमर्थे सेसेनसेअसेन्क्सेकसेनध्यैअध्यैन्कध्यैकध्यैन्शध्यैशध्यैन्तवैतवेङ्तवेनः
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tin_pratyaya_gate_eligible

_GATE_KEY: str = "3_4_9_tumarTe_9"


def cond(state: State) -> bool:
    return tin_pratyaya_gate_eligible(state, "3.4.9", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tumarTe sesenaseasenksekasenaDyEaDyEnkaDyEkaDyEnSaDyESaDyEntavEtaveNtavenaH",
    text_dev              = "तुमर्थे सेसेनसेअसेन्क्सेकसेनध्यैअध्यैन्कध्यैकध्यैन्शध्यैशध्यैन्तवैतवेङ्तवेनः",
    padaccheda_dev        = "तुमर्थे से-सेन्-असे-असेन्-क्से-कसेन्-अध्यै-अध्यैन्-कध्यै-कध्यैन्-शध्यै-शध्यैन्-तवै-तवेङ्-तवेनः",
    why_dev               = "धातोः प्रत्ययः (३.4.9)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
