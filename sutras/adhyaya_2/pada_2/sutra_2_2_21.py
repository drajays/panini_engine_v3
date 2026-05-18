"""
2.2.21  तृतीयाप्रभृतीन्यन्यतरस्याम्  —  VIDHI

Padaccheda: तृतीया-प्रभृतीनि अन्यतरस्याम्

tritiya onwards are optionally compounded.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_21_tritiya_vibhasa"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_2_21_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["tatpurusha_kind"]             = "2.2.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tftIyApraBftInyanyatarasyAm",
    text_dev              = "तृतीयाप्रभृतीन्यन्यतरस्याम्",
    padaccheda_dev        = "तृतीया-प्रभृतीनि अन्यतरस्याम्",
    why_dev               = "तृतीया-प्रभृतीनि अन्यतरस्यां समस्यन्ते (२.२.२१)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
