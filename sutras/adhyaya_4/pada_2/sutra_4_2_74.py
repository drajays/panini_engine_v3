"""
4.2.74  उदक् च विपाशः  —  VIDHI

Padaccheda: उदक् च विपाशः

उदक् च विपाशः (4.2.74)
Pāṭha: ashtadhyayi.com data.txt row i=42074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_74_udak_74"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.74", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "udak ca vipASaH",
    text_dev              = "उदक् च विपाशः",
    samagra_slp1          = "vipASaH udak kUpezu tadasminnastIti deSe tannAmni  tena nirvfttam  tasya nivAsaH  adUraBavaSca iti prAgdIvyatIyaH pratyayaH aY",
    samagra_dev           = "विपाशः उदक् कूपेषु 'तदस्मिन्नस्तीति देशे तन्नाम्नि , तेन निर्वृत्तम् , तस्य निवासः , अदूरभवश्च' (इति) प्राग्दीव्यतीयः प्रत्ययः अञ्",
    padaccheda_dev        = "उदक् च विपाशः",
    why_dev               = "(सूत्रम् 4.2.74) उदक् च विपाशः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
