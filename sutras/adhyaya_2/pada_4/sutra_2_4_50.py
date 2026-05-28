"""
2.4.50  विभाषा लुङ्लृङोः  —  VIDHI

Padaccheda: विभाषा लुङ्-लृङोः

Optional in lun and lrng.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "2_4_50_vibhasa_lung_lrng"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return adhikara_in_effect("2.4.50", state, "2.4.35")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["adesha_kind"]             = "2.4.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzA luNlfNoH",
    text_dev              = "विभाषा लुङ्लृङोः",
    padaccheda_dev        = "विभाषा लुङ्-लृङोः",
    why_dev               = "विभाषा लुङ्-लृङोः (२.४.५०)।",
    anuvritti_from        = ('2.4.49',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
