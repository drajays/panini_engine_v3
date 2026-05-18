"""
7.3.62  प्रयाजानुयाजौ यज्ञाङ्गे  —  VIDHI

Padaccheda: प्रयाज-अनुयाजौ यज्ञाङ्गे

प्रयाजानुयाजौ यज्ञाङ्गे (7.3.62)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "7_3_62_prayAjAnuy_62"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("7_3_62_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.62"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.62",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prayAjAnuyAjO yajYANge",
    text_dev              = "प्रयाजानुयाजौ यज्ञाङ्गे",
    padaccheda_dev        = "प्रयाज-अनुयाजौ यज्ञाङ्गे",
    why_dev               = "(सूत्रम् 7.3.62) प्रयाजानुयाजौ यज्ञाङ्गे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
