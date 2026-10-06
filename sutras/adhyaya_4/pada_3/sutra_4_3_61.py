"""
4.3.61  ग्रामात् पर्यनुपूर्वात्  —  VIDHI

Padaccheda: ग्रामात् परि-अनु-पूर्वात्

ग्रामात् पर्यनुपूर्वात् (4.3.61)
Pāṭha: ashtadhyayi.com data.txt row i=43061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_61_grAmAt_61"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.61", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "grAmAt paryanupUrvAt",
    text_dev              = "ग्रामात् पर्यनुपूर्वात्",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA grAmAt pari-anu-pUrvAt BavaH tatra avyayIBAvAt ca WaY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा ग्रामात् परि-अनु-पूर्वात् भवः तत्र अव्ययीभावात् च ठञ्",
    padaccheda_dev        = "ग्रामात् परि-अनु-पूर्वात्",
    why_dev               = "(सूत्रम् 4.3.61) ग्रामात् पर्यनुपूर्वात्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
