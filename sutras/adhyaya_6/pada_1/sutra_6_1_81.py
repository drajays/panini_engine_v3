"""
6.1.81  क्षय्यजय्यौ शक्यार्थे  —  VIDHI

Padaccheda: क्षय्य-जय्यौ शक्य-अर्थे

क्षय्यजय्यौ शक्यार्थे (6.1.81)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "6_1_81_kzayyajayy_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    # Structural: aṅga present
    if any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("6_1_81_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kzayyajayyO SakyArTe",
    text_dev              = "क्षय्यजय्यौ शक्यार्थे",
    padaccheda_dev        = "क्षय्य-जय्यौ शक्य-अर्थे",
    why_dev               = "(सूत्रम् 6.1.81) क्षय्यजय्यौ शक्यार्थे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
