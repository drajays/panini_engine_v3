"""
4.1.60  दिक्पूर्वपदान्ङीप्  —  VIDHI

Padaccheda: दिक्-पूर्वपदात् ङीप्

दिक्पूर्वपदान्ङीप् (4.1.60)
Pāṭha: ashtadhyayi.com data.txt row i=41060 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_60_dikpUrvapa_60"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.60", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.60"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.60",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dikpUrvapadAnNIp",
    text_dev              = "दिक्पूर्वपदान्ङीप्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt dik-pUrvapadAt NIp NIz",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् दिक्-पूर्वपदात् ङीप् ङीष्",
    padaccheda_dev        = "दिक्-पूर्वपदात् ङीप्",
    why_dev               = "(सूत्रम् 4.1.60) दिक्पूर्वपदान्ङीप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
