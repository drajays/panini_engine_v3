"""
2.3.5  कालाध्वनोरत्यन्तसंयोगे  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: कालाध्वनोः / अत्यन्तसंयोगे

Śāstra: in the sense of *atyantasaṃyoga* (uninterrupted / continuous extent),
the second vibhakti (accusative) is used with nouns denoting time (*kāla*)
or path/distance (*adhvan*).

Engine: registers the kāla/adhvan + atyantasaṃyoga→dvitīyā gate. ``cond``
checks only the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_5_kaladhvanoh_atyantasamyoge"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.5",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "kAlADvanor atyantasaMyoge",
    text_dev              = "कालाध्वनोरत्यन्तसंयोगे",
    padaccheda_dev        = "कालाध्वनोः / अत्यन्तसंयोगे",
    why_dev               = (
        "काल-अध्वनोः अत्यन्तसंयोगे द्वितीया-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.2"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
