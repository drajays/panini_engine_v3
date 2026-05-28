"""
8.3.114  प्रतिस्तब्धनिस्तब्धौ च  —  VIDHI

Padaccheda: प्रतिस्तब्ध-निस्तब्धौ च

प्रतिस्तब्धनिस्तब्धौ च (8.3.114)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_114_pratistabD_114"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_114_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.114"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.114",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pratistabDanistabDO ca",
    text_dev              = "प्रतिस्तब्धनिस्तब्धौ च",
    padaccheda_dev        = "प्रतिस्तब्ध-निस्तब्धौ च",
    why_dev               = "(सूत्रम् 8.3.114) प्रतिस्तब्धनिस्तब्धौ च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
