"""
4.2.9  वामदेवाड्ड्यड्ड्यौ  —  VIDHI

Padaccheda: वामदेवात् ड्यत्-ड्यौ

वामदेवाड्ड्यड्ड्यौ (4.2.9)
Pāṭha: ashtadhyayi.com data.txt row i=42009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_9_vAmadevAqq_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.9", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vAmadevAqqyaqqyO",
    text_dev              = "वामदेवाड्ड्यड्ड्यौ",
    samagra_slp1          = "tena dfzwaM sAma iti vAmadevAt qyat-qyO",
    samagra_dev           = "'तेन दृष्टं साम' (इति)  वामदेवात् ड्यत्-ड्यौ",
    padaccheda_dev        = "वामदेवात् ड्यत्-ड्यौ",
    why_dev               = "(सूत्रम् 4.2.9) वामदेवाड्ड्यड्ड्यौ।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
