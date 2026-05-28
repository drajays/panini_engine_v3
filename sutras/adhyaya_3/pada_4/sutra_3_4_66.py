"""
3.4.66  पर्याप्तिवचनेष्वलमर्थेषु  —  VIDHI

Padaccheda: पर्याप्तिवचनेषु अलम्-अर्थेषु

krt-suffix rule: पर्याप्तिवचनेष्वलमर्थेषु
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_4_66_paryAptiva_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.4.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.4.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "paryAptivacanezvalamarTezu",
    text_dev              = "पर्याप्तिवचनेष्वलमर्थेषु",
    padaccheda_dev        = "पर्याप्तिवचनेषु अलम्-अर्थेषु",
    why_dev               = "धातोः प्रत्ययः (३.4.66)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
