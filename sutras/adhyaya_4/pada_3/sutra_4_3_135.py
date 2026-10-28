"""
4.3.135  अवयवे च प्राण्योषधिवृक्षेभ्यः  —  VIDHI

Padaccheda: अवयवे च प्राणि-ओषधि-वृक्षेभ्यः

अवयवे च प्राण्योषधिवृक्षेभ्यः (4.3.135)
Pāṭha: ashtadhyayi.com data.txt row i=43135 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_135_avayave_135"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.135", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.135"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape
from engine.vivaksha import vivaksita
def _new_cond(state: State) -> bool:
    return (stem_ends_tape(state) and vivaksita(state, "taddhitArtha", "avayava") and not frame_open(state, "avayava")
            and any(x in state.terms[-1].tags for x in ("lex:prANi", "lex:ozaDi", "lex:vfkza")))


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        state.adhikara_stack.append({"id": "4.3.135", "scope_end": "4.3.168", "artha": "avayava", "text_dev": "avayava"})
        if not frame_open(state, "vikAra"):
            state.adhikara_stack.append({"id": "4.3.134", "scope_end": "4.3.168", "artha": "vikAra", "text_dev": "vikAra"})      # cakāra: vikāra too
        if not frame_open(state, "Seza"):
            state.adhikara_stack.append({"id": "4.2.92", "scope_end": "4.3.134", "artha": "Seza", "text_dev": "शेषे"})
        return state
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.135",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "avayave ca prARyozaDivfkzeByaH",
    text_dev              = "अवयवे च प्राण्योषधिवृक्षेभ्यः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA avayave ca prARi-ozaDi-vfkzeByaH tasya idam vikAraH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा अवयवे च प्राणि-ओषधि-वृक्षेभ्यः तस्य इदम् विकारः",
    padaccheda_dev        = "अवयवे च प्राणि-ओषधि-वृक्षेभ्यः",
    why_dev               = "(सूत्रम् 4.3.135) अवयवे च प्राण्योषधिवृक्षेभ्यः।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
