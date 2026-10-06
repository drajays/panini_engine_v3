"""
4.4.131  वेशोयशआदेर्भगाद्यल्  —  VIDHI

Padaccheda: वेशोयश-आदेः भगात् यल्

वेशोयशआदेर्भगाद्यल् (4.4.131)
Pāṭha: ashtadhyayi.com data.txt row i=44131 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_131_veSoyaSaAd_131"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.131", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.131"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.131",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "veSoyaSaAderBagAdyal",
    text_dev              = "वेशोयशआदेर्भगाद्यल्",
    samagra_slp1          = "veSo-yaSa-AdeH BagAt matvarTe Candasi saMjYAyAm yal",
    samagra_dev           = "वेशो-यश-आदेः भगात् मत्वर्थे छन्दसि संज्ञायाम् यल्",
    padaccheda_dev        = "वेशोयश-आदेः भगात् यल्",
    why_dev               = "(सूत्रम् 4.4.131) वेशोयशआदेर्भगाद्यल्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
