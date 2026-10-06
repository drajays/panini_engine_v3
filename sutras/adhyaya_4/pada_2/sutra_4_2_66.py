"""
4.2.66  छन्दोब्राह्मणानि च तद्विषयाणि  —  VIDHI

Padaccheda: छन्दोब्राह्मणानि च तद्विषयाणि

छन्दोब्राह्मणानि च तद्विषयाणि (4.2.66)
Pāṭha: ashtadhyayi.com data.txt row i=42066 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_2_66_CandobrAhm_66"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.2.66", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.2.66"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.2.66",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "CandobrAhmaRAni ca tadvizayARi",
    text_dev              = "छन्दोब्राह्मणानि च तद्विषयाणि",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA Candas-brAhmaRAni ca tad-vizayARi tat aDIte veda proktAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा छन्दस्-ब्राह्मणानि च तद्-विषयाणि तत् अधीते वेद प्रोक्तात्",
    padaccheda_dev        = "छन्दोब्राह्मणानि च तद्विषयाणि",
    why_dev               = "(सूत्रम् 4.2.66) छन्दोब्राह्मणानि च तद्विषयाणि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
