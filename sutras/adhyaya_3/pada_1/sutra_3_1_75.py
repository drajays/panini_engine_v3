"""
3.1.75  अक्षोऽन्यतरस्याम्  —  VIDHI

Padaccheda: अक्षः अन्यतरस्याम्

Krt suffix rule from dhatu: अक्षोऽन्यतरस्याम् (75)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_75_akzonyatara_75"


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
    state.meta["krt_kind"] = "3.1.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "akzo'nyatarasyAm",
    text_dev              = "अक्षोऽन्यतरस्याम्",
    padaccheda_dev        = "अक्षः अन्यतरस्याम्",
    why_dev               = "धातोः [अक्षोऽन्यतरस्याम्]-प्रत्ययः विहितः (३.१.75)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
