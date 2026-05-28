"""
2.4.44  आत्मनेपदेष्वन्यतरस्याम्  —  VIDHI

Padaccheda: आत्मनेपदेषु अन्यतरस्याम्

Optional in atmanepada forms.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_44_atmane_anyatara"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.44", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmanepadezvanyatarasyAm",
    text_dev              = "आत्मनेपदेष्वन्यतरस्याम्",
    padaccheda_dev        = "आत्मनेपदेषु अन्यतरस्याम्",
    why_dev               = "आत्मनेपदेषु अन्यतरस्याम् (२.४.४४)।",
    anuvritti_from        = ('2.4.42',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
