"""
4.2.21  साऽस्मिन् पौर्णमासीति (संज्ञायाम्)  —  VIDHI

Padaccheda: सा अस्मिन् पौर्णमासि इति (संज्ञायाम्)

साऽस्मिन् पौर्णमासीति (संज्ञायाम्) (4.2.21)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_21_sAsmin_21"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_21_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sA'smin pOrRamAsIti (saMjYAyAm)",
    text_dev              = "साऽस्मिन् पौर्णमासीति (संज्ञायाम्)",
    padaccheda_dev        = "सा अस्मिन् पौर्णमासि इति (संज्ञायाम्)",
    why_dev               = "(सूत्रम् 4.2.21) साऽस्मिन् पौर्णमासीति (संज्ञायाम्)।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
