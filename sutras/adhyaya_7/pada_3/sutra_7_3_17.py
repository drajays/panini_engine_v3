"""
7.3.17  परिमाणान्तस्यासंज्ञाशाणयोः  —  VIDHI

Padaccheda: परिमाण-अन्तस्य असंज्ञाशाणयोः

परिमाणान्तस्यासंज्ञाशाणयोः (7.3.17)
Pāṭha: ashtadhyayi.com data.txt row i=73017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_17_parimARAnt_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.17", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "parimARAntasyAsaMjYASARayoH",
    text_dev              = "परिमाणान्तस्यासंज्ञाशाणयोः",
    samagra_slp1          = "aNgasya uttarapadasya parimARAntasya asaMjYASARayoH vfdDiH YRiti acaH tadDitezu AdeH SvAdeH saMKyAyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य परिमाणान्तस्य असंज्ञाशाणयोः वृद्धिः ञ्णिति अचः तद्धितेषु आदेः श्वादेः संख्यायाः",
    padaccheda_dev        = "परिमाण-अन्तस्य असंज्ञाशाणयोः",
    why_dev               = "(सूत्रम् 7.3.17) परिमाणान्तस्यासंज्ञाशाणयोः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
