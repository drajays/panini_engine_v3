"""
6.1.22  स्फायः स्फी निष्ठायाम्  —  VIDHI

Padaccheda: स्फायः स्फी (लुप्तप्रथमान्तनिर्देशः) निष्ठायाम्

स्फायः स्फी निष्ठायाम् (6.1.22)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_22_sPAyaH_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.22",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sPAyaH sPI nizWAyAm",
    text_dev              = "स्फायः स्फी निष्ठायाम्",
    padaccheda_dev        = "स्फायः स्फी (लुप्तप्रथमान्तनिर्देशः) निष्ठायाम्",
    why_dev               = "(सूत्रम् 6.1.22) स्फायः स्फी निष्ठायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
