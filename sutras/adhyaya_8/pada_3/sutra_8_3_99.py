"""
8.3.99  ऐति संज्ञायामगात्  —  VIDHI

Padaccheda: एति संज्ञायाम् अ-गात्

ऐति संज्ञायामगात् (8.3.99)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_99_Eti_99"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_99_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.99"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.99",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Eti saMjYAyAmagAt",
    text_dev              = "ऐति संज्ञायामगात्",
    padaccheda_dev        = "एति संज्ञायाम् अ-गात्",
    why_dev               = "(सूत्रम् 8.3.99) ऐति संज्ञायामगात्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
