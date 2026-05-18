"""
5.2.115  अत इनिठनौ  —  VIDHI

Padaccheda: अतः इनि-ठनौ

अत इनिठनौ (5.2.115)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "5_2_115_ata_115"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("5_2_115_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.115"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.115",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ata iniWanO",
    text_dev              = "अत इनिठनौ",
    padaccheda_dev        = "अतः इनि-ठनौ",
    why_dev               = "(सूत्रम् 5.2.115) अत इनिठनौ।",
    anuvritti_from        = ('5.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
