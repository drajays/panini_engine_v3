"""
4.1.17  प्राचां ष्फ तद्धितः  —  VIDHI

Padaccheda: प्राचाम् ष्फः तद्धितः

प्राचां ष्फ तद्धितः (4.1.17)
Pāṭha: ashtadhyayi.com data.txt row i=41017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_17_prAcAM_17"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.17", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prAcAM zPa tadDitaH",
    text_dev              = "प्राचां ष्फ तद्धितः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt prAcAm zPaH tadDitaH NIp yaYaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् प्राचाम् ष्फः तद्धितः ङीप् यञः",
    padaccheda_dev        = "प्राचाम् ष्फः तद्धितः",
    why_dev               = "(सूत्रम् 4.1.17) प्राचां ष्फ तद्धितः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
