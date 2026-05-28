"""
3.2.103  सुयजोर्ङ्वनिप्  —  VIDHI

Padaccheda: सु-यजोः ङ्वनिप्

krt-suffix rule: सुयजोर्ङ्वनिप् (103)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_103_suyajorNva_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: kṛt context — dhātu present, no kṛt pratyaya yet
    if (any("dhatu" in t.tags for t in state.terms)
            and not any("krt" in t.tags and "pratyaya" in t.tags
                        for t in state.terms)):
        return True
    return bool(state.meta.get("3_2_103_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "suyajorNvanip",
    text_dev              = "सुयजोर्ङ्वनिप्",
    padaccheda_dev        = "सु-यजोः ङ्वनिप्",
    why_dev               = "धातोः कृत्-प्रत्ययः [सुयजोर्ङ्वनिप्] विहितः (३.२.103)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
