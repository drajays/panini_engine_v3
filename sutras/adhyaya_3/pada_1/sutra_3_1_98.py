"""
3.1.98  पोरदुपधात्  —  VIDHI

Padaccheda: पोः अत्-उपधात्

Krt suffix rule from dhatu: पोरदुपधात् (98)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_98_poradupaDAt_98"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_98_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.98"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.98",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "poradupaDAt",
    text_dev              = "पोरदुपधात्",
    padaccheda_dev        = "पोः अत्-उपधात्",
    why_dev               = "धातोः [पोरदुपधात्]-प्रत्ययः विहितः (३.१.98)।",
    anuvritti_from        = ('3.1.1', '3.1.92'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
