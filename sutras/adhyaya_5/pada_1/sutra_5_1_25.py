"""
5.1.25  कंसाट्टिठन्  —  VIDHI

Padaccheda: कंसात् टिठन्

कंसाट्टिठन् (5.1.25)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_1_25_kaMsAwwiWa_25"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_1_25_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.25"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.25",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kaMsAwwiWan",
    text_dev              = "कंसाट्टिठन्",
    padaccheda_dev        = "कंसात् टिठन्",
    why_dev               = "(सूत्रम् 5.1.25) कंसाट्टिठन्।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
