"""
6.2.105  उत्तरपदवृद्धौ सर्वं च  —  VIDHI

Padaccheda: उत्तरपद-वृद्धौ सर्वम् च

उत्तरपदवृद्धौ सर्वं च (6.2.105)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_2_105_uttarapada_105"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any(t.varnas for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttarapadavfdDO sarvaM ca",
    text_dev              = "उत्तरपदवृद्धौ सर्वं च",
    padaccheda_dev        = "उत्तरपद-वृद्धौ सर्वम् च",
    why_dev               = "(सूत्रम् 6.2.105) उत्तरपदवृद्धौ सर्वं च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
