"""
6.1.182  न गोश्वन्त्साववर्णराडङ्क्रुङ्कृद्भ्यः  —  VIDHI

Padaccheda: न गो-श्वन्-सौ-अवर्ण-राट्-अङ्-क्रुङ्-कृद्‍भ्यः

न गोश्वन्त्साववर्णराडङ्क्रुङ्कृद्भ्यः (6.1.182)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_182_na_182"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_182_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.182"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.182",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "na goSvantsAvavarRarAqaNkruNkfdByaH",
    text_dev              = "न गोश्वन्त्साववर्णराडङ्क्रुङ्कृद्भ्यः",
    padaccheda_dev        = "न गो-श्वन्-सौ-अवर्ण-राट्-अङ्-क्रुङ्-कृद्‍भ्यः",
    why_dev               = "(सूत्रम् 6.1.182) न गोश्वन्त्साववर्णराडङ्क्रुङ्कृद्भ्यः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
