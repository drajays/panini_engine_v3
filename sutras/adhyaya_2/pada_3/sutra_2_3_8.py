"""
2.3.8  कर्मप्रवचनीययुक्ते द्वितीया  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: कर्मप्रवचनीय-युक्ते / द्वितीया

Śāstra: when used with a *karmapravacanīya* (a particle that governs an object
in the manner of a verbal prefix, cf. 1.4.83-98), the second vibhakti
(accusative/dvitīyā) is prescribed for the governed noun.

Engine: registers the karmapravacanīya-yukta→dvitīyā gate. ``cond`` checks
only the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_8_karmapravachaniya_yukte_dvitiya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.8",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "karmapravachanIyayukte dvitIyA",
    text_dev              = "कर्मप्रवचनीययुक्ते द्वितीया",
    padaccheda_dev        = "कर्मप्रवचनीय-युक्ते / द्वितीया",
    why_dev               = (
        "कर्मप्रवचनीय-युक्ते द्वितीया-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.2"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
