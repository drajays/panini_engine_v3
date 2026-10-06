"""
5.2.9  अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु  —  VIDHI

Padaccheda: अनुपद-सर्वान्न-अय-अनयम् बद्धा-भक्षयति-नेयेषु

अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु (5.2.9)
Pāṭha: ashtadhyayi.com data.txt row i=52009 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_2_9_anupadasar_9"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.2.9", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.2.9"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.2.9",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anupadasarvAnnAyAnayaM badDABakzayatineyezu",
    text_dev              = "अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु",
    samagra_slp1          = "tat anupada-sarvAnna-ayAnayam badDA-Bakzayati-neyezu KaH",
    samagra_dev           = "तत् अनुपद-सर्वान्न-अयानयम् बद्धा-भक्षयति-नेयेषु खः",
    padaccheda_dev        = "अनुपद-सर्वान्न-अय-अनयम् बद्धा-भक्षयति-नेयेषु",
    why_dev               = "(सूत्रम् 5.2.9) अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
