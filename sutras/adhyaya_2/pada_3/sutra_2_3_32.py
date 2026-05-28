"""
2.3.32  पृथग्विनानानाभिस्तृतीयाऽन्यतरस्याम्  —  VIDHI

Padaccheda: पृथक्-विना-नानाभिः तृतीया अन्यतरस्याम्

prthak vina nana optionally take tritiya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_32_prthak_vina_nana"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("2_3_32_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.32"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.32",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pfTagvinAnAnABistftIyA'nyatarasyAm",
    text_dev              = "पृथग्विनानानाभिस्तृतीयाऽन्यतरस्याम्",
    padaccheda_dev        = "पृथक्-विना-नानाभिः तृतीया अन्यतरस्याम्",
    why_dev               = "पृथक्-विना-नानाभिः तृतीया अन्यतरस्याम् (२.३.३२)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
