"""
2.3.14  क्रियार्थोपपदस्य च कर्मणि स्थानिनः  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: क्रियार्थ-उपदस्य / च / कर्मणि / स्थानिनः

Śāstra: the fourth vibhakti (dative/caturthī) is also prescribed for the karma
of a *kriyārthopapadā* (a noun that is an upapadā expressing the purpose of the
action, i.e. a purpose/goal noun), specifically for the *sthānin* (the antecedent
whose karma is in view).

Engine: registers the kriyārthopapadā-karma-sthānin→caturthī gate. ``cond``
checks only the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_14_kriyartha_upapadasa_karmani_sthanina"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.14",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "kriyArtTopapadasya ca karmaRi sTAninaH",
    text_dev              = "क्रियार्थोपपदस्य च कर्मणि स्थानिनः",
    padaccheda_dev        = "क्रियार्थ-उपदस्य / च / कर्मणि / स्थानिनः",
    why_dev               = (
        "क्रियार्थोपदस्य स्थानिनः कर्मणि चतुर्थी च — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.13"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
