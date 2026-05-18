"""
2.1.50  दिक्संख्ये संज्ञायाम्  —  VIDHI

Padaccheda: दिक्सङ्ख्ये संज्ञायाम्

Direction and number words in samjna context form karmadharaya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_1_50_dik_samkhya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_1_50_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["karmadharaya_kind"]             = "2.1.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.1.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "diksaMKye saMjYAyAm",
    text_dev              = "दिक्संख्ये संज्ञायाम्",
    padaccheda_dev        = "दिक्सङ्ख्ये संज्ञायाम्",
    why_dev               = "दिक्-संख्ये संज्ञायां कर्मधारयः (२.१.५०)।",
    anuvritti_from        = ('2.1.3',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
