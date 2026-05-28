"""
8.3.80  समासेऽङ्गुलेः सङ्गः  —  VIDHI

Padaccheda: समासे अङ्‍गुलेः सङ्गः (षष्ठ्याः स्थाने प्रथमाऽत्र व्यत्ययेन )

समासेऽङ्गुलेः सङ्गः (8.3.80)
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "8_3_80_samAseNgu_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if state.tripadi_zone and any("anga" in t.tags or t.varnas for t in state.terms):
        return True
    return bool(state.meta.get("8_3_80_arm"))


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "samAse'NguleH saNgaH",
    text_dev              = "समासेऽङ्गुलेः सङ्गः",
    padaccheda_dev        = "समासे अङ्‍गुलेः सङ्गः (षष्ठ्याः स्थाने प्रथमाऽत्र व्यत्ययेन )",
    why_dev               = "(सूत्रम् 8.3.80) समासेऽङ्गुलेः सङ्गः।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
