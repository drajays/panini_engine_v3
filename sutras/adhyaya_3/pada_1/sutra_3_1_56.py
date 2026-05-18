"""
3.1.56  सर्त्तिशास्त्यर्तिभ्यश्च  —  VIDHI

Padaccheda: सर्त्ति-शास्ति-अर्तिभ्यः च

Krt suffix rule from dhatu: सर्त्तिशास्त्यर्तिभ्यश्च (56)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_1_56_sarttiSAstya_56"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_1_56_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.1.56"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.1.56",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarttiSAstyartiByaSca",
    text_dev              = "सर्त्तिशास्त्यर्तिभ्यश्च",
    padaccheda_dev        = "सर्त्ति-शास्ति-अर्तिभ्यः च",
    why_dev               = "धातोः [सर्त्तिशास्त्यर्तिभ्यश्च]-प्रत्ययः विहितः (३.१.56)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
