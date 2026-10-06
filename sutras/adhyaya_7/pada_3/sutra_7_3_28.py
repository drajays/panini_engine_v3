"""
7.3.28  प्रवाहणस्य ढे  —  VIDHI

Padaccheda: प्रवाहणस्य ढे

प्रवाहणस्य ढे (7.3.28)
Pāṭha: ashtadhyayi.com data.txt row i=73028 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_28_pravAhaRas_28"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.28", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pravAhaRasya Qe",
    text_dev              = "प्रवाहणस्य ढे",
    samagra_slp1          = "aNgasya uttarapadasya pravAhaRasya Qe vfdDiH YRiti acaH tadDitezu AdeH pUrvasya tu vA parimARasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य प्रवाहणस्य ढे वृद्धिः ञ्णिति अचः तद्धितेषु आदेः पूर्वस्य तु वा परिमाणस्य",
    padaccheda_dev        = "प्रवाहणस्य ढे",
    why_dev               = "(सूत्रम् 7.3.28) प्रवाहणस्य ढे।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
