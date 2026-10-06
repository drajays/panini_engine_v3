"""
5.2.111  काण्डाण्डादीरन्नीरचौ  —  VIDHI

Padaccheda: काण्ड-अण्डात् ईरन्-ईरचौ

काण्डाण्डादीरन्नीरचौ (5.2.111)
Pāṭha: ashtadhyayi.com data.txt row i=52111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_111_kARqARqAdI_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.111", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kARqARqAdIrannIracO",
    text_dev              = "काण्डाण्डादीरन्नीरचौ",
    samagra_slp1          = "tat asya asmin astIti iti kARqa-aRqAt Iran-IracO",
    samagra_dev           = "'तत् अस्य, अस्मिन् अस्तीति' (इति) काण्ड-अण्डात् ईरन्-ईरचौ",
    padaccheda_dev        = "काण्ड-अण्डात् ईरन्-ईरचौ",
    why_dev               = "(सूत्रम् 5.2.111) काण्डाण्डादीरन्नीरचौ।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
