"""
3.3.97  ऊतियूतिजूतिसातिहेतिकीर्तयश्च  —  VIDHI

Padaccheda: ऊति-यूति-जूति-साति-हेति-कीर्त्तयः च

krt-suffix rule: ऊतियूतिजूतिसातिहेतिकीर्तयश्च
Pāṭha: ashtadhyayi.com data.txt row i=33097 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_97_UtiyUtijUt_97"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.97", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.97"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.97",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "UtiyUtijUtisAtihetikIrtayaSca",
    text_dev              = "ऊतियूतिजूतिसातिहेतिकीर्तयश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm Uti-yUti-jUti-sAti-heti-kIrtayaH ca kft ktin udAttaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् ऊति-यूति-जूति-साति-हेति-कीर्तयः च कृत् क्तिन् उदात्तः",
    padaccheda_dev        = "ऊति-यूति-जूति-साति-हेति-कीर्त्तयः च",
    why_dev               = "धातोः प्रत्ययः (३.3.97)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
