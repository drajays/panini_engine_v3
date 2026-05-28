"""
2.4.37  लुङ्सनोर्घसॢ  —  VIDHI

Padaccheda: लुङ्-सनोः घसॢ

ghasl replaces adas in lun and san.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_37_lung_sana_ghasl"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.37", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.37",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "luNsanorGasx",
    text_dev              = "लुङ्सनोर्घसॢ",
    padaccheda_dev        = "लुङ्-सनोः घसॢ",
    why_dev               = "लुङ्-सनोः घसॢ (२.४.३७)।",
    anuvritti_from        = ('2.4.35',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
