"""
4.1.70  संहितशफलक्षणवामादेश्च  —  VIDHI

Padaccheda: संहित-शफ-लक्षण-वाम-आदेः च

संहितशफलक्षणवामादेश्च (4.1.70)
Pāṭha: ashtadhyayi.com data.txt row i=41070 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_70_saMhitaSaP_70"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.70", state, "4.1.1"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.70"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.70",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saMhitaSaPalakzaRavAmAdeSca",
    text_dev              = "संहितशफलक्षणवामादेश्च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt striyAm anupasarjanAt saMhita-SaPalakzaRa-vAmAdeH ca UN UrU-uttarapadAt",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् स्त्रियाम् अनुपसर्जनात् संहित-शफलक्षण-वामादेः च ऊङ् ऊरू-उत्तरपदात्",
    padaccheda_dev        = "संहित-शफ-लक्षण-वाम-आदेः च",
    why_dev               = "(सूत्रम् 4.1.70) संहितशफलक्षणवामादेश्च।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
