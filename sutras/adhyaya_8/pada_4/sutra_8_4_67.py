"""
8.4.67  नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्  —  VIDHI

Padaccheda: नः उदात्त-स्वरित-उदयम् अ-गार्ग्य-काश्यप-गालवानाम्

नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम् (8.4.67)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_67_nodAttasva_67"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_67_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nodAttasvaritodayamagArgyakASyapagAlavAnAm",
    text_dev              = "नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्",
    padaccheda_dev        = "नः उदात्त-स्वरित-उदयम् अ-गार्ग्य-काश्यप-गालवानाम्",
    why_dev               = "(सूत्रम् 8.4.67) नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
