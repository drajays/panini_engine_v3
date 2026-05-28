"""
3.1.132  चित्याग्निचित्ये च  —  VIDHI

Padaccheda: चित्य-अग्निचित्ये च

Krt suffix rule from dhatu: चित्याग्निचित्ये च (132)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_132_cityAgnicity_132"


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
    state.meta["krt_kind"] = "3.1.132"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.132",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cityAgnicitye ca",
    text_dev              = "चित्याग्निचित्ये च",
    padaccheda_dev        = "चित्य-अग्निचित्ये च",
    why_dev               = "धातोः [चित्याग्निचित्ये च]-प्रत्ययः विहितः (३.१.132)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
