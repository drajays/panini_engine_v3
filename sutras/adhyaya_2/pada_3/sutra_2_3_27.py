"""
2.3.27  सर्वनाम्नस्तृतीया च  —  VIDHI

Padaccheda: सर्वनाम्नः तृतीया च

Sarvanaaman also takes tritiya.
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_3_27_sarvanaman_tritiya"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return state.meta.get("2_3_27_arm") is True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.27"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.27",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "sarvanAmnastftIyA ca",
    text_dev              = "सर्वनाम्नस्तृतीया च",
    padaccheda_dev        = "सर्वनाम्नः तृतीया च",
    why_dev               = "सर्वनाम्नः तृतीया च (२.३.२७)।",
    anuvritti_from        = ('2.3.18',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
