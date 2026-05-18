"""
2.3.6  अपवर्गे तृतीया  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: अपवर्गे / तृतीया

Śāstra: in the sense of *apavarga* (completion / termination of an action),
the third vibhakti (instrumental/tṛtīyā) is used with nouns denoting the
measure of time or path at the completion-point.

Engine: registers the apavarga→tṛtīyā gate. ``cond`` checks only the gate
flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_6_apavarge_trtiya"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.6",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "apavarge tftIyA",
    text_dev              = "अपवर्गे तृतीया",
    padaccheda_dev        = "अपवर्गे / तृतीया",
    why_dev               = (
        "अपवर्गे (क्रियासमाप्तौ) काल-अध्वनोः तृतीया-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
