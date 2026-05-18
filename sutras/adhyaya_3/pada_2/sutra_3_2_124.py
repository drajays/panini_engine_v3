"""
3.2.124  लटः शतृशानचावप्रथमासमानाधिकरणे  —  VIDHI

Padaccheda: लटः शतृ-शानचः अ-प्रथमा-समानाधिकरणे

krt-suffix rule: लटः शतृशानचावप्रथमासमानाधिकरणे (124)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "3_2_124_lawaH_124"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("3_2_124_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "lawaH SatfSAnacAvapraTamAsamAnADikaraRe",
    text_dev              = "लटः शतृशानचावप्रथमासमानाधिकरणे",
    padaccheda_dev        = "लटः शतृ-शानचः अ-प्रथमा-समानाधिकरणे",
    why_dev               = "धातोः कृत्-प्रत्ययः [लटः शतृशानचावप्रथमासमानाधिकरणे] विहितः (३.२.124)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
