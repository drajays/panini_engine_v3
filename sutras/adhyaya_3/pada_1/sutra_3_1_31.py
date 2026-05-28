"""
3.1.31  आयादय आर्धद्धातुके वा  —  VIDHI

Padaccheda: आय्-आदयः आर्धधातुके वा

Krt suffix rule from dhatu: आयादय आर्धद्धातुके वा (31)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_31_AyAdaya_31"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_31_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.31"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.31",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AyAdaya ArDadDAtuke vA",
    text_dev              = "आयादय आर्धद्धातुके वा",
    padaccheda_dev        = "आय्-आदयः आर्धधातुके वा",
    why_dev               = "धातोः [आयादय आर्धद्धातुके वा]-प्रत्ययः विहितः (३.१.31)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
