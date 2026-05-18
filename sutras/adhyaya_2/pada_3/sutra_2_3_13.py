"""
2.3.13  चतुर्थी सम्प्रदाने  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: चतुर्थी / सम्प्रदाने

Śāstra: the fourth vibhakti (dative/caturthī) is prescribed for the sampradāna
kāraka (the recipient, the one for whose benefit the action is done; cf. 1.4.32).

Engine: registers the sampradāna→caturthī gate. ``cond`` checks only the gate
flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_13_caturthI_sampradane"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.13",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "caturTI sampradAne",
    text_dev              = "चतुर्थी सम्प्रदाने",
    padaccheda_dev        = "चतुर्थी / सम्प्रदाने",
    why_dev               = (
        "सम्प्रदान-कारके चतुर्थी-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
