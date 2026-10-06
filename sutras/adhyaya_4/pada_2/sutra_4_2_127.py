"""
4.2.127  धूमादिभ्यश्च  —  VIDHI

Padaccheda: धूम-आदिभ्यः च

धूमादिभ्यश्च (4.2.127)
Pāṭha: ashtadhyayi.com data.txt row i=42127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_127_DUmAdiByaS_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.127", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "DUmAdiByaSca",
    text_dev              = "धूमादिभ्यश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA DUma-AdiByaH ca vuY",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा धूम-आदिभ्यः च वुञ्",
    padaccheda_dev        = "धूम-आदिभ्यः च",
    why_dev               = "(सूत्रम् 4.2.127) धूमादिभ्यश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
