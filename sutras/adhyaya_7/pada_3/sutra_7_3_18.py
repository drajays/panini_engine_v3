"""
7.3.18  जे प्रोष्ठपदानाम्  —  VIDHI

Padaccheda: जे प्रोष्ठपदानाम्

जे प्रोष्ठपदानाम् (7.3.18)
Pāṭha: ashtadhyayi.com data.txt row i=73018 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_3_18_je_18"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.3.18", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.3.18"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.3.18",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "je prozWapadAnAm",
    text_dev              = "जे प्रोष्ठपदानाम्",
    samagra_slp1          = "aNgasya uttarapadasya je prozWapadAnAm vfdDiH acaH YRiti tadDitezu AdeH SvAdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य उत्तरपदस्य जे प्रोष्ठपदानाम् वृद्धिः अचः ञ्णिति तद्धितेषु आदेः श्वादेः",
    padaccheda_dev        = "जे प्रोष्ठपदानाम्",
    why_dev               = "(सूत्रम् 7.3.18) जे प्रोष्ठपदानाम्।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
