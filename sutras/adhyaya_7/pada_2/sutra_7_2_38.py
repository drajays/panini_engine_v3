"""
7.2.38  वॄतो वा  —  VIDHI

Padaccheda: वॄतः वा

वॄतो वा (7.2.38)
Pāṭha: ashtadhyayi.com data.txt row i=72038 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_38_vFto_38"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.38", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.38"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.38",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vFto vA",
    text_dev              = "वॄतो वा",
    samagra_slp1          = "aNgasya vFtaH vA valAdeH iw ArDaDAtukasya grahaH aliwi dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य वॄतः वा वलादेः इट् आर्धधातुकस्य ग्रहः अलिटि दीर्घः",
    padaccheda_dev        = "वॄतः वा",
    why_dev               = "(सूत्रम् 7.2.38) वॄतो वा।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
