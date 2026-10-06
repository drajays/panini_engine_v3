"""
4.2.78  रोणी  —  VIDHI

Padaccheda: रोणी

रोणी (4.2.78)
Pāṭha: ashtadhyayi.com data.txt row i=42078 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_78_roRI_78"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.78", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.78"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.78",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "roRI",
    text_dev              = "रोणी",
    samagra_slp1          = "roRyAH tadasminnastIti deSe tannAmni  tena nirvfttam  tasya nivAsaH  adUraBavaSca iti prAgdIvyatIyaH pratyayaH aR",
    samagra_dev           = "रोण्याः  'तदस्मिन्नस्तीति देशे तन्नाम्नि , तेन निर्वृत्तम् , तस्य निवासः , अदूरभवश्च' (इति) प्राग्दीव्यतीयः प्रत्ययः अण्",
    padaccheda_dev        = "रोणी",
    why_dev               = "(सूत्रम् 4.2.78) रोणी।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
