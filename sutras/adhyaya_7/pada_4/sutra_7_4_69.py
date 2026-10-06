"""
7.4.69  दीर्घ इणः किति  —  VIDHI

Padaccheda: दीर्घः इणः किति

दीर्घ इणः किति (7.4.69)
Pāṭha: ashtadhyayi.com data.txt row i=74069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "7_4_69_dIrGa_69"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if adhikara_in_effect("7.4.69", state, "6.4.1") and any("anga" in t.tags for t in state.terms):
        return True

def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "7.4.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "7.4.69",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "dIrGa iRaH kiti",
    text_dev              = "दीर्घ इणः किति",
    samagra_slp1          = "aNgasya aByAsasya dIrGaH iRaH kiti liwi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य अभ्यासस्य दीर्घः इणः किति लिटि",
    padaccheda_dev        = "दीर्घः इणः किति",
    why_dev               = "(सूत्रम् 7.4.69) दीर्घ इणः किति।",
    anuvritti_from        = ('7.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
