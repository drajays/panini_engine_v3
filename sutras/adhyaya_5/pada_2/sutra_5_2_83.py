"""
5.2.83  कुल्माषादञ्  —  VIDHI

Padaccheda: कुल्माषात् अञ्

कुल्माषादञ् (5.2.83)
Pāṭha: ashtadhyayi.com data.txt row i=52083 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_83_kulmAzAdaY_83"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.83", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kulmAzAdaY",
    text_dev              = "कुल्माषादञ्",
    samagra_slp1          = "tat annamasmin iti saMjYAyAm kulmAzAt prAye aY",
    samagra_dev           = "'तत् अन्नमस्मिन्' (इति) संज्ञायाम् कुल्माषात्  प्राये अञ्",
    padaccheda_dev        = "कुल्माषात् अञ्",
    why_dev               = "(सूत्रम् 5.2.83) कुल्माषादञ्।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
