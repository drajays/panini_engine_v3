"""
7.2.43  ऋतश्च संयोगादेः  —  VIDHI

Padaccheda: ऋतः च संयोग-आदेः

ऋतश्च संयोगादेः (7.2.43)
Pāṭha: ashtadhyayi.com data.txt row i=72043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_2_43_ftaSca_43"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.2.43", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.2.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.2.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ftaSca saMyogAdeH",
    text_dev              = "ऋतश्च संयोगादेः",
    samagra_slp1          = "aNgasya ftaH ca saMyogAdeH valAdeH iw ArDaDAtukasya vA liNsicoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य ऋतः च संयोगादेः वलादेः इट् आर्धधातुकस्य वा लिङ्सिचोः",
    padaccheda_dev        = "ऋतः च संयोग-आदेः",
    why_dev               = "(सूत्रम् 7.2.43) ऋतश्च संयोगादेः।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
