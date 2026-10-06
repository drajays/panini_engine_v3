"""
4.2.75  संकलादिभ्यश्च  —  VIDHI

Padaccheda: सङ्कल-आदिभ्यः च

संकलादिभ्यश्च (4.2.75)
Pāṭha: ashtadhyayi.com data.txt row i=42075 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_75_saMkalAdiB_75"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.75", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.75"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.75",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMkalAdiByaSca",
    text_dev              = "संकलादिभ्यश्च",
    samagra_slp1          = "saNkalAdiByaH tadasminnastIti deSe tannAmni  tena nirvfttam  tasya nivAsaH  adUraBavaSca iti prAgdIvyatIyaH pratyayaH aY",
    samagra_dev           = "सङ्कलादिभ्यः 'तदस्मिन्नस्तीति देशे तन्नाम्नि , तेन निर्वृत्तम् , तस्य निवासः , अदूरभवश्च' (इति) प्राग्दीव्यतीयः प्रत्ययः अञ्",
    padaccheda_dev        = "सङ्कल-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.2.75) संकलादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
