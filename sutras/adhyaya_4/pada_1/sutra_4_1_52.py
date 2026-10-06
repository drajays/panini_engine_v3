"""
4.1.52  बहुव्रीहेश्चान्तोदात्तात्  —  VIDHI

Padaccheda: बहुव्रीहेः च अन्त-उदात्तात्

बहुव्रीहेश्चान्तोदात्तात् (4.1.52)
Pāṭha: ashtadhyayi.com data.txt row i=41052 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_52_bahuvrIheS_52"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.52", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "bahuvrIheScAntodAttAt",
    text_dev              = "बहुव्रीहेश्चान्तोदात्तात्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt bahuvrIheH ca antodAttAt NIz ktAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् बहुव्रीहेः च अन्तोदात्तात् ङीष् क्तात्",
    padaccheda_dev        = "बहुव्रीहेः च अन्त-उदात्तात्",
    why_dev               = "(सूत्रम् 4.1.52) बहुव्रीहेश्चान्तोदात्तात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
