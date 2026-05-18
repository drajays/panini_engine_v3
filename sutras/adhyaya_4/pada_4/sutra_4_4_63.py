"""
4.4.63  कर्माध्ययने वृत्तम्  —  VIDHI

Padaccheda: कर्म अध्ययने वृत्तम्

कर्माध्ययने वृत्तम् (4.4.63)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_4_63_karmADyaya_63"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_4_63_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.63"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.63",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmADyayane vfttam",
    text_dev              = "कर्माध्ययने वृत्तम्",
    padaccheda_dev        = "कर्म अध्ययने वृत्तम्",
    why_dev               = "(सूत्रम् 4.4.63) कर्माध्ययने वृत्तम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
