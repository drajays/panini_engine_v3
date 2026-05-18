"""
2.3.11  प्रतिनिधिप्रतिदाने च यस्मात्  —  VIDHI (kāraka-vibhakti gate)

Padaccheda: प्रतिनिधि / प्रतिदाने / च / यस्मात्

Śāstra: the fifth vibhakti (ablative/pañcamī) is also used (in addition to
dvitīyā) in the senses of *pratinidhi* (substitute / replacement) and
*pratidāna* (counter-gift / recompense), from whatever is taken in substitution.

Engine: registers the pratinidhi/pratidāna→pañcamī gate. ``cond`` checks only
the gate flag, never vibhakti coordinates (CONSTITUTION Art. 2).
``r1_form_identity_exempt=True``.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

GATE_KEY = "2_3_11_pratinidhi_pratidane_pancami"


def cond(state: State) -> bool:
    return state.paribhasha_gates.get(GATE_KEY) is not True


def act(state: State) -> State:
    state.paribhasha_gates[GATE_KEY] = True
    state.samjna_registry[GATE_KEY]  = True
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.11",
    sutra_type            = SutraType.VIDHI,
    text_slp1             = "pratiniDipratidAne ca yasmAt",
    text_dev              = "प्रतिनिधिप्रतिदाने च यस्मात्",
    padaccheda_dev        = "प्रतिनिधि / प्रतिदाने / च / यस्मात्",
    why_dev               = (
        "प्रतिनिधि-प्रतिदाने यस्मात् पञ्चमी च — "
        "कारक-विभक्ति-गेट-रूपेण निबद्धम् (आर्ट. २)।"
    ),
    anuvritti_from        = ("2.3.1", "2.3.10"),
    cond                  = cond,
    act                   = act,
    r1_form_identity_exempt = True,
)

register_sutra(SUTRA)
