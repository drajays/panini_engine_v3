"""
8.2.70  अम्नरूधरवरित्युभयथा छन्दसि  —  VIDHI

Padaccheda: अम्नः-ऊधः-अवर् (लुप्तषष्ठ्यन्तनिर्देशः) इति उभयथा छन्दसि

अम्नरूधरवरित्युभयथा छन्दसि (8.2.70)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_2_70_amnarUDara_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_2_70_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "amnarUDaravarityuBayaTA Candasi",
    text_dev              = "अम्नरूधरवरित्युभयथा छन्दसि",
    padaccheda_dev        = "अम्नः-ऊधः-अवर् (लुप्तषष्ठ्यन्तनिर्देशः) इति उभयथा छन्दसि",
    why_dev               = "(सूत्रम् 8.2.70) अम्नरूधरवरित्युभयथा छन्दसि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
