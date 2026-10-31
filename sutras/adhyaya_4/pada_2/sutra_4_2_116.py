"""
4.2.116  काश्यादिभ्यष्ठञ्ञिठौ  —  VIDHI

Padaccheda: काशि-आदिभ्यः ठञ्-ञिठौ

काश्यादिभ्यष्ठञ्ञिठौ (4.2.116)
Pāṭha: ashtadhyayi.com data.txt row i=42116 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.taddhita_attach import taddhita_site, attach_taddhita

_UPA = "WaY"      # ṭhañ; ñiṭh is the same ṭh with the ñ and the uccāraṇa vowel exchanged (Kāśikā), so the stem is the same; the two differ only in svara and in the strī (kāśikī / kāśikā): not modelled, see docs/PLAN_TADDHITA_FIX.md


def _site(state: State):
    return taddhita_site(state, "Seza", gana_name="kASyAdiH")      # the Gaṇapāṭha's kāśi-ādi; the listed words take it though not vṛddha (vacanaprāmāṇyāt)


def cond(state: State) -> bool:
    return _site(state) is not None


def act(state: State) -> State:
    if _site(state) is None:
        return state
    return attach_taddhita(state, _UPA)


SUTRA = SutraRecord(
    sutra_id              = "4.2.116",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kASyAdiByazWaYYiWO",
    text_dev              = "काश्यादिभ्यष्ठञ्ञिठौ",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA kASI-AdiByaH WaY-YiWO vfdDAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा काशी-आदिभ्यः ठञ्-ञिठौ वृद्धात्",
    padaccheda_dev        = "काशि-आदिभ्यः ठञ्-ञिठौ",
    why_dev               = "(सूत्रम् 4.2.116) काश्यादिभ्यष्ठञ्ञिठौ।",
    anuvritti_from        = ('4.1.1',),
    apavada_of            = ('4.2.114', '4.1.83'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
