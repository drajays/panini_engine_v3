"""
3.3.96  मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः  —  VIDHI

Padaccheda: मन्त्रे वृष-इष-पच-मन-विद-भू-वी-राः (पञ्चम्यर्थे प्रथमा) उदात्तः

krt-suffix rule: मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः
Pāṭha: ashtadhyayi.com data.txt row i=33096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_96_mantre_96"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.96", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mantre vfzezapacamanavidaBUvIrA udAttaH",
    text_dev              = "मन्त्रे वृषेषपचमनविदभूवीरा उदात्तः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BAve akartari ca kArake saMjYAyAm striyAm mantre vfza-iza-paca-mana-vida-BU-vI-rAH udAttaH kft ktin",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भावे अकर्तरि च कारके संज्ञायाम् स्त्रियाम् मन्त्रे वृष-इष-पच-मन-विद-भू-वी-राः उदात्तः कृत् क्तिन्",
    padaccheda_dev        = "मन्त्रे वृष-इष-पच-मन-विद-भू-वी-राः (पञ्चम्यर्थे प्रथमा) उदात्तः",
    why_dev               = "धातोः प्रत्ययः (३.3.96)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
