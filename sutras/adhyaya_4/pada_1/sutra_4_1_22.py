"""
4.1.22  अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि  —  VIDHI

Padaccheda: अपरिमाण-बिस्त-अचित-कम्बल्येभ्यः न तद्धित-लुकि

अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि (4.1.22)
Pāṭha: ashtadhyayi.com data.txt row i=41022 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_22_aparimARab_22"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.22", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.22"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.22",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "aparimARabistAcitakambalyeByo na tadDitaluki",
    text_dev              = "अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt a-parimARa-bista-Acita-kambalyeByaH na tadDita-luki NIp dvigoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् अ-परिमाण-बिस्त-आचित-कम्बल्येभ्यः न तद्धित-लुकि ङीप् द्विगोः",
    padaccheda_dev        = "अपरिमाण-बिस्त-अचित-कम्बल्येभ्यः न तद्धित-लुकि",
    why_dev               = "(सूत्रम् 4.1.22) अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
