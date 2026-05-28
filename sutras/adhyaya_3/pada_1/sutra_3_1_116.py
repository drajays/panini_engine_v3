"""
3.1.116  पुष्यसिद्ध्यौ नक्षत्रे  —  VIDHI

Padaccheda: पुष्य-सिद्ध्यौ नक्षत्रे

Krt suffix rule from dhatu: पुष्यसिद्ध्यौ नक्षत्रे (116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_116_puzyasidDyO_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "puzyasidDyO nakzatre",
    text_dev              = "पुष्यसिद्ध्यौ नक्षत्रे",
    padaccheda_dev        = "पुष्य-सिद्ध्यौ नक्षत्रे",
    why_dev               = "धातोः [पुष्यसिद्ध्यौ नक्षत्रे]-प्रत्ययः विहितः (३.१.116)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
