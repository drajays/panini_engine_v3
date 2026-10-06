"""
7.4.80  ओः पुयण्ज्यपरे  —  VIDHI

Padaccheda: ओः पु-यण्-जि अ-परे

ओः पुयण्ज्यपरे (7.4.80)
Pāṭha: ashtadhyayi.com data.txt row i=74080 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_80_oH_80"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.80", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.80"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.80",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "oH puyaRjyapare",
    text_dev              = "ओः पुयण्ज्यपरे",
    samagra_slp1          = "aNgasya aByAsasya oH puyaRji apare it sani",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य ओः पुयण्जि अपरे इत् सनि",
    padaccheda_dev        = "ओः पु-यण्-जि अ-परे",
    why_dev               = "(सूत्रम् 7.4.80) ओः पुयण्ज्यपरे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
