"""
4.2.44  अनुदात्तादेरञ्  —  VIDHI

Padaccheda: अनुदात्त-आदेः अञ्

अनुदात्तादेरञ् (4.2.44)
Pāṭha: ashtadhyayi.com data.txt row i=42044 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_44_anudAttAde_44"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.44", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.44"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.44",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anudAttAderaY",
    text_dev              = "अनुदात्तादेरञ्",
    samagra_slp1          = "tasya samUhaH iti anudAttAdeH aY",
    samagra_dev           = "तस्य समूहः (इति) अनुदात्तादेः अञ्",
    padaccheda_dev        = "अनुदात्त-आदेः अञ्",
    why_dev               = "(सूत्रम् 4.2.44) अनुदात्तादेरञ्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
