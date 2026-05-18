"""
2.3.2  कर्मणि द्वितीया  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: कर्मणि / द्वितीया

Śāstra: when the semantic role is karma (direct object / अनभिहित kāraka),
the second vibhakti (accusative sup) is prescribed.

Engine: this sūtra registers the karma→dvitīyā mapping in
``state.paribhasha_gates`` and ``state.samjna_registry``. It is a gate rule;
``cond`` checks only that the gate has not yet been set — it never reads
``state.meta['vibhakti']`` or any paradigm coordinate (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True`` because this sūtra records a semantic mapping,
not a surface phonemic change.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_2_karmani_dvitiya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.2",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "karmaRi dvitIyA",
    text_dev              = "कर्मणि द्वितीया",
    padaccheda_dev        = "कर्मणि / द्वितीया",
    why_dev               = (
        "कर्म-कारके (अनभिहिते) द्वितीया-विभक्तिः विधीयते — "
        "इह यन्त्रे कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
