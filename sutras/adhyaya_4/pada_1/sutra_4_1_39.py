"""
4.1.39  वर्णादनुदात्तात्तोपधात्तो नः  —  VIDHI

Padaccheda: वर्णात् अनुदात्तात् त-उपधात् तः नः

वर्णादनुदात्तात्तोपधात्तो नः (4.1.39)
Pāṭha: ashtadhyayi.com data.txt row i=41039 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_39_varRAdanud_39"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.39", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "varRAdanudAttAttopaDAtto naH",
    text_dev              = "वर्णादनुदात्तात्तोपधात्तो नः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt varRAt anudAttAt ta-upaDAt taH naH vA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् वर्णात् अनुदात्तात् त-उपधात् तः नः वा",
    padaccheda_dev        = "वर्णात् अनुदात्तात् त-उपधात् तः नः",
    why_dev               = "(सूत्रम् 4.1.39) वर्णादनुदात्तात्तोपधात्तो नः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
