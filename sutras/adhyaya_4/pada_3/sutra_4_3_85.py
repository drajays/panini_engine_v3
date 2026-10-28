"""
4.3.85  तद्गच्छति पथिदूतयोः  —  VIDHI

Padaccheda: तत् गच्छति (क्रियापदम्) पथि-दूतयोः

तद्गच्छति पथिदूतयोः (4.3.85)
Pāṭha: ashtadhyayi.com data.txt row i=43085 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_85_tadgacCati_85"


def _legacy_cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.85", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def _legacy_act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.85"
    return state



from engine.taddhita_attach import frame_open, stem_ends_tape
from engine.vivaksha import vivaksita
def _new_cond(state: State) -> bool:
    return stem_ends_tape(state) and vivaksita(state, "taddhitArtha", "gacCatiPaTiDUta") and not frame_open(state, "gacCatiPaTiDUta")


def cond(state: State) -> bool:
    return _new_cond(state) or _legacy_cond(state)


def act(state: State) -> State:
    if _new_cond(state):
        # the sense, and the śeṣa group it lies in (4.2.92 … 4.3.134): aṇ comes from 4.1.83, the specials of both read these frames
        state.adhikara_stack.append({"id": "4.3.85", "scope_end": "4.3.134", "artha": "gacCatiPaTiDUta", "text_dev": "gacCatiPaTiDUta"})
        if not frame_open(state, "Seza"):
            state.adhikara_stack.append({"id": "4.2.92", "scope_end": "4.3.134", "artha": "Seza", "text_dev": "शेषे"})
        return state
    return _legacy_act(state)


SUTRA = SutraRecord(
    sutra_id              = "4.3.85",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tadgacCati paTidUtayoH",
    text_dev              = "तद्गच्छति पथिदूतयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA tat gacCati paTidUtayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा तत् गच्छति पथिदूतयोः",
    padaccheda_dev        = "तत् गच्छति (क्रियापदम्) पथि-दूतयोः",
    why_dev               = "(सूत्रम् 4.3.85) तद्गच्छति पथिदूतयोः।",
    anuvritti_from        = ('4.1.1',),
    also_vidhi     = True,          # the loop opens this sense-frame / attaches from the speaker's taddhitArtha
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
