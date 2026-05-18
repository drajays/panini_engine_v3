"""
4.2.48  केशाश्वाभ्यां यञ्छावन्यतरस्याम्  —  VIDHI

Padaccheda: केश-अश्वाभ्याम् यञ्-छौ अन्यतरस्याम्

केशाश्वाभ्यां यञ्छावन्यतरस्याम् (4.2.48)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "4_2_48_keSASvAByA_48"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("4_2_48_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.48"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.48",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "keSASvAByAM yaYCAvanyatarasyAm",
    text_dev              = "केशाश्वाभ्यां यञ्छावन्यतरस्याम्",
    padaccheda_dev        = "केश-अश्वाभ्याम् यञ्-छौ अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 4.2.48) केशाश्वाभ्यां यञ्छावन्यतरस्याम्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
