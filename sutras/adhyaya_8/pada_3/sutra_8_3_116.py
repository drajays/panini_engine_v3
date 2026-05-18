"""
8.3.116  स्तम्भुसिवुसहां चङि  —  VIDHI

Padaccheda: स्तम्भु-सिवु-सहाम् चङि

स्तम्भुसिवुसहां चङि (8.3.116)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_116_stamBusivu_116"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_3_116_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.116"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "stamBusivusahAM caNi",
    text_dev              = "स्तम्भुसिवुसहां चङि",
    padaccheda_dev        = "स्तम्भु-सिवु-सहाम् चङि",
    why_dev               = "(सूत्रम् 8.3.116) स्तम्भुसिवुसहां चङि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
