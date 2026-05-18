"""
8.1.46  एहिमन्ये प्रहासे लृट्  —  VIDHI

Padaccheda: एहिमन्ये (लुप्तप्रथमान्तनिर्देशः) प्रहासे लृट्

एहिमन्ये प्रहासे लृट् (8.1.46)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_1_46_ehimanye_46"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("8_1_46_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.46"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.46",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ehimanye prahAse lfw",
    text_dev              = "एहिमन्ये प्रहासे लृट्",
    padaccheda_dev        = "एहिमन्ये (लुप्तप्रथमान्तनिर्देशः) प्रहासे लृट्",
    why_dev               = "(सूत्रम् 8.1.46) एहिमन्ये प्रहासे लृट्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
