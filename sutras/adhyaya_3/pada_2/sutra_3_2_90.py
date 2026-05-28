"""
3.2.90  सोमे सुञः  —  VIDHI

Padaccheda: सोमे सुञः

krt-suffix rule: सोमे सुञः (90)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_90_some_90"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_90_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.90"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.90",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "some suYaH",
    text_dev              = "सोमे सुञः",
    padaccheda_dev        = "सोमे सुञः",
    why_dev               = "धातोः कृत्-प्रत्ययः [सोमे सुञः] विहितः (३.२.90)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
