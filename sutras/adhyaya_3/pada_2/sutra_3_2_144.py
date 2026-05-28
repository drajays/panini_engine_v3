"""
3.2.144  अपे च लषः  —  VIDHI

Padaccheda: अपे च लषः

krt-suffix rule: अपे च लषः (144)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_144_ape_144"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_144_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.144"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ape ca lazaH",
    text_dev              = "अपे च लषः",
    padaccheda_dev        = "अपे च लषः",
    why_dev               = "धातोः कृत्-प्रत्ययः [अपे च लषः] विहितः (३.२.144)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
