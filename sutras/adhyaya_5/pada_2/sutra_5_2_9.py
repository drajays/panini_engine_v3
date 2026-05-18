"""
5.2.9  अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु  —  VIDHI

Padaccheda: अनुपद-सर्वान्न-अय-अनयम् बद्धा-भक्षयति-नेयेषु

अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु (5.2.9)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_9_anupadasar_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_9_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupadasarvAnnAyAnayaM badDABakzayatineyezu",
    text_dev              = "अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु",
    padaccheda_dev        = "अनुपद-सर्वान्न-अय-अनयम् बद्धा-भक्षयति-नेयेषु",
    why_dev               = "(सूत्रम् 5.2.9) अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
