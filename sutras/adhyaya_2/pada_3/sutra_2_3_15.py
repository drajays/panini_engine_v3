"""
2.3.15  तुमर्थाच्च भाववचनात्  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: तुमर्थात् / च / भाववचनात्

Śāstra: the fourth vibhakti (dative/caturthī) is also prescribed from a noun
that is *tumarthā* (expressive of purpose, equivalent to a *tum*-infinitive)
or from a *bhāvavacana* (abstract/action noun).

Engine: registers the tumārtha/bhāvavacana→caturthī gate. ``cond`` checks only
the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_15_tumartha_bhavavacana_caturthI"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.15",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tumartAc ca BAvavacanAt",
    text_dev              = "तुमर्थाच्च भाववचनात्",
    padaccheda_dev        = "तुमर्थात् / च / भाववचनात्",
    why_dev               = (
        "तुमर्थात् भाववचनाच्च चतुर्थी — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.13"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
