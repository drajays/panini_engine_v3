"""
4.3.100  जनपदिनां जनपदवत् सर्वं जनपदेन समानशब्दानां बहुवचने  —  VIDHI

Padaccheda: जनपदिनाम् जनपद-वत् सर्वम् जनपदेन समानशब्दानाम् बहुवचने

जनपदिनां जनपदवत् सर्वं जनपदेन समानशब्दानां बहुवचने (4.3.100)
Pāṭha: ashtadhyayi.com data.txt row i=43100 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_100_janapadinA_100"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.100", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.100"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.100",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janapadinAM janapadavat sarvaM janapadena samAnaSabdAnAM bahuvacane",
    text_dev              = "जनपदिनां जनपदवत् सर्वं जनपदेन समानशब्दानां बहुवचने",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA janapadinAm janapadavat sarvam janapadena samAna-SabdAnAm bahuvacane saH asya BaktiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा जनपदिनाम् जनपदवत् सर्वम् जनपदेन समान-शब्दानाम् बहुवचने सः अस्य भक्तिः",
    padaccheda_dev        = "जनपदिनाम् जनपद-वत् सर्वम् जनपदेन समानशब्दानाम् बहुवचने",
    why_dev               = "(सूत्रम् 4.3.100) जनपदिनां जनपदवत् सर्वं जनपदेन समानशब्दानां बहुवचने।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
