"""
4.3.162  माने वयः  —  VIDHI

Padaccheda: माने वयः

माने वयः (4.3.162)
Pāṭha: ashtadhyayi.com data.txt row i=43162 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_162_mAne_162"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.162", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.162"
    return state



from phonology import mk
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _site(state: State):
    return taddhita_site(state, "vikAra", stems=frozenset({"dru"}))


def _new_cond(state: State) -> bool:
    return _site(state) is not None and vivaksita(state, "vikAraBeda", "mAna")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        return attach_taddhita(state, "vaya")
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.162",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "mAne vayaH",
    text_dev              = "माने वयः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA mAne vayaH vikAraH tasya avayave droH ca",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा माने वयः विकारः तस्य अवयवे द्रोः च",
    padaccheda_dev        = "माने वयः",
    why_dev               = "(सूत्रम् 4.3.162) माने वयः।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.3.161',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
