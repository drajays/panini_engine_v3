"""
7.1.76  छन्दस्यपि दृश्यते  —  VIDHI

Padaccheda: छन्दसि अपि दृश्यते (क्रियापदम्)

छन्दस्यपि दृश्यते (7.1.76)
Pāṭha: ashtadhyayi.com data.txt row i=71076 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_1_76_Candasyapi_76"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.1.76", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.1.76"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.1.76",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Candasyapi dfSyate",
    text_dev              = "छन्दस्यपि दृश्यते",
    samagra_slp1          = "aNgasya Candasi api dfSyate num napuMsakasya udAttaH asTi-daDi-sakTi-akzRAm anaN",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य छन्दसि अपि दृश्यते नुम् नपुंसकस्य उदात्तः अस्थि-दधि-सक्थि-अक्ष्णाम् अनङ्",
    padaccheda_dev        = "छन्दसि अपि दृश्यते (क्रियापदम्)",
    why_dev               = "(सूत्रम् 7.1.76) छन्दस्यपि दृश्यते।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
