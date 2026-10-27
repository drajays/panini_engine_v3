"""
4.3.144  नित्यं वृद्धशरादिभ्यः  —  VIDHI

Padaccheda: नित्यम् वृद्ध-शर-आदिभ्यः

नित्यं वृद्धशरादिभ्यः (4.3.144)
Pāṭha: ashtadhyayi.com data.txt row i=43144 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_144_nityaM_144"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.144", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.144"
    return state



from engine.taddhita_attach import taddhita_site, attach_taddhita
def _site(state: State):
    return taddhita_site(state, "vikAra", has_tag="vṛddha") or taddhita_site(state, "vikAra", gana_of="4.3.144")


def _new_cond(state: State) -> bool:
    return _site(state) is not None


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _site(state) is not None:
        return attach_taddhita(state, "mayaw")
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.144",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nityaM vfdDaSarAdiByaH",
    text_dev              = "नित्यं वृद्धशरादिभ्यः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA nityam vfdDa-Sara-AdiByaH vikAraH tasya avayave BAzAyAm a-Bakzya-AcCAdanayoH mayaw",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा नित्यम् वृद्ध-शर-आदिभ्यः विकारः तस्य अवयवे भाषायाम् अ-भक्ष्य-आच्छादनयोः मयट्",
    padaccheda_dev        = "नित्यम् वृद्ध-शर-आदिभ्यः",
    why_dev               = "(सूत्रम् 4.3.144) नित्यं वृद्धशरादिभ्यः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
