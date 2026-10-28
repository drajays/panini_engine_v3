"""
4.3.154  प्राणिरजतादिभ्योऽञ्  —  VIDHI

Padaccheda: प्राणि-रजत-आदिभ्यः अञ्

प्राणिरजतादिभ्योऽञ् (4.3.154)
Pāṭha: ashtadhyayi.com data.txt row i=43154 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_154_prARirajat_154"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.154", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.154"
    return state



from phonology import mk
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _site(state: State):
    return taddhita_site(state, "vikAra", gana_of="4.3.154")


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        return attach_taddhita(state, "aY")
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.154",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'prARirajatAdiByoY',
    text_dev              = 'प्राणिरजतादिभ्योऽञ्',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA prARi-rajata-AdiByaH aY tasya vikAraH avayave",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा प्राणि-रजत-आदिभ्यः अञ् तस्य विकारः अवयवे",
    padaccheda_dev        = "प्राणि-रजत-आदिभ्यः अञ्",
    why_dev               = "(सूत्रम् 4.3.154) प्राणिरजतादिभ्योऽञ्।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83', '4.3.137', '4.3.143', '4.3.144'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
