"""
3.1.65  तपोऽनुतापे च  —  VIDHI

Padaccheda: तपः अनुतापे च

Krt suffix rule from dhatu: तपोऽनुतापे च (65)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_65_taponutApe_65"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_1_65_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.65"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.65",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tapo'nutApe ca",
    text_dev              = "तपोऽनुतापे च",
    padaccheda_dev        = "तपः अनुतापे च",
    why_dev               = "धातोः [तपोऽनुतापे च]-प्रत्ययः विहितः (३.१.65)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
