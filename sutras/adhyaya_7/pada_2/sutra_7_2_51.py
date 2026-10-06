"""
7.2.51  पूङश्च  —  VIDHI

Padaccheda: पूङः च

पूङश्च (7.2.51)
Pāṭha: ashtadhyayi.com data.txt row i=72051 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_51_pUNaSca_51"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.51", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.51"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.51",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pUNaSca",
    text_dev              = "पूङश्च",
    samagra_slp1          = "aNgasya pUNaH ca valAdeH iw ArDaDAtukasya vA ktvAnizWayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य पूङः च वलादेः इट् आर्धधातुकस्य वा क्त्वानिष्ठयोः",
    padaccheda_dev        = "पूङः च",
    why_dev               = "(सूत्रम् 7.2.51) पूङश्च।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
