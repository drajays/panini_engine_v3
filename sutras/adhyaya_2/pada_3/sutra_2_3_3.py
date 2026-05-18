"""
2.3.3  तृतीया च होश्छन्दसि  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: तृतीया / च / होः / छन्दसि

Śāstra: in the Vedic register (chandas), the third vibhakti (instrumental)
is also used for karma (in addition to dvitīyā). The particle *hoḥ*
(ablative of *ho*, calling-particle) triggers this alternant.

Engine: registers the chandas-karma→tṛtīyā gate. ``cond`` checks only
that the gate has not yet been opened; it does not read vibhakti coordinates
(CONSTITUTION Art. 2). ``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_3_trtiya_chandasi"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.3",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "tftIyA ca hoH chandasi",
    text_dev              = "तृतीया च होश्छन्दसि",
    padaccheda_dev        = "तृतीया / च / होः / छन्दसि",
    why_dev               = (
        "छन्दसि होः-योगे कर्म-कारके तृतीया च — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.2"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
