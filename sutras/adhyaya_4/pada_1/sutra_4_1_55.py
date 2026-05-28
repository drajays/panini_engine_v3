"""
4.1.55  नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च  —  VIDHI

Padaccheda: नासिका-उदर-ओष्ठ-जङ्‍घा-दन्त-कर्ण-शृङ्गात् च

नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च (4.1.55)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_55_nAsikodarO_55"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.55", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.55"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.55",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nAsikodarOzWajaNGAdantakarRaSfNgAcca",
    text_dev              = "नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च",
    padaccheda_dev        = "नासिका-उदर-ओष्ठ-जङ्‍घा-दन्त-कर्ण-शृङ्गात् च",
    why_dev               = "(सूत्रम् 4.1.55) नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
