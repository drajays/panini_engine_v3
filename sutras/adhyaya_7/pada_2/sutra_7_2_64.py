"""
7.2.64  बभूथाततन्थजगृम्भववर्थेति निगमे  —  VIDHI

Padaccheda: बभूथ (लुप्तप्रथमान्तनिर्देशः) आततन्थ (लुप्तप्रथमान्तनिर्देशः) जगृम्भ (लुप्तप्रथमान्तनिर्देशः) ववर्थ (लुप्तप्रथमान्तनिर्देशः) इति निगमे

बभूथाततन्थजगृम्भववर्थेति निगमे (7.2.64)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_64_baBUTAtata_64"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.64", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True
    return bool(state.meta.get("7_2_64_arm"))

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "baBUTAtatanTajagfmBavavarTeti nigame",
    text_dev              = "बभूथाततन्थजगृम्भववर्थेति निगमे",
    padaccheda_dev        = "बभूथ (लुप्तप्रथमान्तनिर्देशः) आततन्थ (लुप्तप्रथमान्तनिर्देशः) जगृम्भ (लुप्तप्रथमान्तनिर्देशः) ववर्थ (लुप्तप्रथमान्तनिर्देशः) इति निगमे",
    why_dev               = "(सूत्रम् 7.2.64) बभूथाततन्थजगृम्भववर्थेति निगमे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
