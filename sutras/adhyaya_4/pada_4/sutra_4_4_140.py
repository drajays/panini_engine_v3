"""
4.4.140  वसोः समूहे च  —  VIDHI

Padaccheda: वसोः समूहे च

वसोः समूहे च (4.4.140)
Pāṭha: ashtadhyayi.com data.txt row i=44140 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_140_vasoH_140"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.140", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.140"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.140",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vasoH samUhe ca",
    text_dev              = "वसोः समूहे च",
    samagra_slp1          = "vasoH samUhe maye ca Candasi saMjYAyAm yat ",
    samagra_dev           = "वसोः समूहे मये च छन्दसि संज्ञायाम् यत् ।",
    padaccheda_dev        = "वसोः समूहे च",
    why_dev               = "(सूत्रम् 4.4.140) वसोः समूहे च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
