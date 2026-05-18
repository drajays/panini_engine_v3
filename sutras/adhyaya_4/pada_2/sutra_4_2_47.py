"""
4.2.47  अचित्तहस्तिधेनोष्ठक्  —  VIDHI

Padaccheda: अचित्त-हस्ति-धेनोः ठक्

अचित्तहस्तिधेनोष्ठक् (4.2.47)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_47_acittahast_47"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_47_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.47"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.47",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "acittahastiDenozWak",
    text_dev              = "अचित्तहस्तिधेनोष्ठक्",
    padaccheda_dev        = "अचित्त-हस्ति-धेनोः ठक्",
    why_dev               = "(सूत्रम् 4.2.47) अचित्तहस्तिधेनोष्ठक्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
