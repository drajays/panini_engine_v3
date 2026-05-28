"""
8.3.86  अभिनिसः स्तनः शब्दसंज्ञायाम्  —  VIDHI

Padaccheda: अभि-निसः स्तनः शब्दसंज्ञायाम्

अभिनिसः स्तनः शब्दसंज्ञायाम् (8.3.86)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_86_aBinisaH_86"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "aBinisaH stanaH SabdasaMjYAyAm",
    text_dev              = "अभिनिसः स्तनः शब्दसंज्ञायाम्",
    padaccheda_dev        = "अभि-निसः स्तनः शब्दसंज्ञायाम्",
    why_dev               = "(सूत्रम् 8.3.86) अभिनिसः स्तनः शब्दसंज्ञायाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
