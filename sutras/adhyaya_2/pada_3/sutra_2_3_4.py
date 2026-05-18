"""
2.3.4  अन्तराऽन्तरेण युक्ते  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: अन्तरा / अन्तरेण / युक्ते

Śāstra: when used with the indeclinables *antarā* (between / without) or
*antareṇa* (without / in the absence of), the second vibhakti (dvitīyā /
accusative) is applied to the governed noun.

Engine: registers the antarā/antareṇa-yukta→dvitīyā gate. ``cond`` checks
only the gate flag; it never reads vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_4_antara_antarena_yukte"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.4",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "antarA antareRa yukte",
    text_dev              = "अन्तराऽन्तरेण युक्ते",
    padaccheda_dev        = "अन्तरा / अन्तरेण / युक्ते",
    why_dev               = (
        "अन्तरा/अन्तरेण-युक्ते द्वितीया-विभक्तिः — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1",),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
