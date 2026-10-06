"""
4.1.111  भर्गात् त्रैगर्ते  —  VIDHI

Padaccheda: भर्गात् त्रैगर्ते

भर्गात् त्रैगर्ते (4.1.111)
Pāṭha: ashtadhyayi.com data.txt row i=41111 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_1_111_BargAt_111"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.1.111", state, "4.1.92"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.1.111"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.1.111",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BargAt trEgarte",
    text_dev              = "भर्गात् त्रैगर्ते",
    samagra_slp1          = "tasya gotre apatyam iti trEgarte BargAt PaY",
    samagra_dev           = "'तस्य गोत्रे अपत्यम्' (इति) त्रैगर्ते भर्गात् फञ्",
    padaccheda_dev        = "भर्गात् त्रैगर्ते",
    why_dev               = "(सूत्रम् 4.1.111) भर्गात् त्रैगर्ते।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
