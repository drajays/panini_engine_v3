"""
8.2.80  अदसोऽसेर्दादु दो मः  —  VIDHI

Padaccheda: अदसः अ-सेः दात् उ (लुप्तप्रथमान्तनिर्देशः) दः मः

अदसोऽसेर्दादु दो मः (8.2.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_80_adasoserd_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "adaso'serdAdu do maH",
    text_dev              = "अदसोऽसेर्दादु दो मः",
    padaccheda_dev        = "अदसः अ-सेः दात् उ (लुप्तप्रथमान्तनिर्देशः) दः मः",
    why_dev               = "(सूत्रम् 8.2.80) अदसोऽसेर्दादु दो मः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
