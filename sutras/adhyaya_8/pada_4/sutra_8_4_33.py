"""
8.4.33  वा निंसनिक्षनिन्दाम्  —  VIDHI

Padaccheda: वा निंस-निक्ष-निन्दाम्

वा निंसनिक्षनिन्दाम् (8.4.33)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_33_vA_33"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_33_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA niMsanikzanindAm",
    text_dev              = "वा निंसनिक्षनिन्दाम्",
    padaccheda_dev        = "वा निंस-निक्ष-निन्दाम्",
    why_dev               = "(सूत्रम् 8.4.33) वा निंसनिक्षनिन्दाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
