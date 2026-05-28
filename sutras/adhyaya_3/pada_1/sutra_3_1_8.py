"""
3.1.8  सुप आत्मनः क्यच्  —  VIDHI

Padaccheda: सुप आत्मनः क्यच्

Krt suffix rule from dhatu: सुप आत्मनः क्यच् (8)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_8_supa_8"


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
    state.meta["krt_kind"] = "3.1.8"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.8",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "supa AtmanaH kyac",
    text_dev              = "सुप आत्मनः क्यच्",
    padaccheda_dev        = "सुप आत्मनः क्यच्",
    why_dev               = "धातोः [सुप आत्मनः क्यच्]-प्रत्ययः विहितः (३.१.8)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
