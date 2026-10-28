"""
4.3.165  जम्ब्वा वा  —  VIDHI

Padaccheda: जम्ब्वाः वा

जम्ब्वा वा (4.3.165)
Pāṭha: ashtadhyayi.com data.txt row i=43165 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_165_jambvA_165"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.165", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.165"
    return state



from phonology import mk
from engine.taddhita_attach import taddhita_site, attach_taddhita
from engine.vivaksha import vivaksita
from engine.vikalpa import policy_pick
def _site(state: State):
    return taddhita_site(state, "vikAra", stems=frozenset({"jambU"}))


def _new_cond(state: State) -> bool:
    return _site(state) is not None and vivaksita(state, "vikAraBeda", "Pala")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        if policy_pick(state, "4.3.165", 2) == 1:
            return state                      # vā: the other pratyaya stays a reading
        return attach_taddhita(state, "aR")
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.165",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "jambvA vA",
    text_dev              = "जम्ब्वा वा",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA jambvAH vA vikAraH tasya avayave Pale aR",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा जम्ब्वाः वा विकारः तस्य अवयवे फले अण्",
    padaccheda_dev        = "जम्ब्वाः वा",
    why_dev               = "(सूत्रम् 4.3.165) जम्ब्वा वा।",
    anuvritti_from        = ('4.1.1',),
    apavada_of     = ('4.1.83',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
