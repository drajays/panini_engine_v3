"""
4.4.127  वयस्यासु मूर्ध्नो मतुप्  —  VIDHI

Padaccheda: वयस्यासु मूर्ध्नः मतुप्

वयस्यासु मूर्ध्नो मतुप् (4.4.127)
Pāṭha: ashtadhyayi.com data.txt row i=44127 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_4_127_vayasyAsu_127"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.4.127", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.4.127"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.4.127",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vayasyAsu mUrDno matup",
    text_dev              = "वयस्यासु मूर्ध्नो मतुप्",
    samagra_slp1          = "upaDAnaH mantraH AsAm iti vayasyAsu mUrDnaH iti izwakAsu matup matoH ca luk",
    samagra_dev           = "'उपधानः मन्त्रः आसाम्' (इति) 'वयस्यासु मूर्ध्नः' इति इष्टकासु मतुप्, मतोः च लुक्",
    padaccheda_dev        = "वयस्यासु मूर्ध्नः मतुप्",
    why_dev               = "(सूत्रम् 4.4.127) वयस्यासु मूर्ध्नो मतुप्।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
