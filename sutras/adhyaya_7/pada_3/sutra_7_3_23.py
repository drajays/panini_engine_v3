"""
7.3.23  दीर्घाच्च वरुणस्य  —  VIDHI

Padaccheda: दीर्घात् च वरुणस्य

दीर्घाच्च वरुणस्य (7.3.23)
Pāṭha: ashtadhyayi.com data.txt row i=73023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_23_dIrGAcca_23"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.23", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.23",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGAcca varuRasya",
    text_dev              = "दीर्घाच्च वरुणस्य",
    samagra_slp1          = "aNgasya uttarapadasya dIrGAt ca varuRasya vfdDiH YRiti acaH AdeH tadDitezu pUrvapadasya devatAdvandve na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य दीर्घात् च वरुणस्य वृद्धिः ञ्णिति अचः आदेः तद्धितेषु पूर्वपदस्य देवताद्वन्द्वे न",
    padaccheda_dev        = "दीर्घात् च वरुणस्य",
    why_dev               = "(सूत्रम् 7.3.23) दीर्घाच्च वरुणस्य।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
