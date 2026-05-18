"""
4.1.117  विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु  —  VIDHI

Padaccheda: विकर्ण-शुङ्ग-छगलात् वत्स-भरद्वाज-अत्रिषु

विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु (4.1.117)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_1_117_vikarRaSuN_117"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_1_117_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.117"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.117",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vikarRaSuNgacCagalAdvatsaBaradvAjAtrizu",
    text_dev              = "विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु",
    padaccheda_dev        = "विकर्ण-शुङ्ग-छगलात् वत्स-भरद्वाज-अत्रिषु",
    why_dev               = "(सूत्रम् 4.1.117) विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
