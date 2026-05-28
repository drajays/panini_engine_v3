"""
3.1.9  काम्यच्च  —  VIDHI

Padaccheda: काम्यच् च

Krt suffix rule from dhatu: काम्यच्च (9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_9_kAmyacca_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_9_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kAmyacca",
    text_dev              = "काम्यच्च",
    padaccheda_dev        = "काम्यच् च",
    why_dev               = "धातोः [काम्यच्च]-प्रत्ययः विहितः (३.१.9)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
