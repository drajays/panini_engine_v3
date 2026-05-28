"""
8.4.50  त्रिप्रभृतिषु शाकटायनस्य  —  VIDHI

Padaccheda: त्रिप्रभृतिषु ७/३ शाकटायनस्य ६/१

त्रिप्रभृतिषु शाकटायनस्य (8.4.50)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_4_50_tripraBfti_50"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: relevant term present
    if any(t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_4_50_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.50"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.50",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tripraBftizu SAkawAyanasya",
    text_dev              = "त्रिप्रभृतिषु शाकटायनस्य",
    padaccheda_dev        = "त्रिप्रभृतिषु ७/३ शाकटायनस्य ६/१",
    why_dev               = "(सूत्रम् 8.4.50) त्रिप्रभृतिषु शाकटायनस्य।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
