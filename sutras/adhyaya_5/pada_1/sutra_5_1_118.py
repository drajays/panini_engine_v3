"""
5.1.118  उपसर्गाच्छन्दसि धात्वर्थे  —  VIDHI

Padaccheda: उपसर्गात् छन्दसि धातु-अर्थे

उपसर्गाच्छन्दसि धात्वर्थे (5.1.118)
Pāṭha: ashtadhyayi.com data.txt row i=51118 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_1_118_upasargAcC_118"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.1.118", state, "4.1.82"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.1.118"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.1.118",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "upasargAcCandasi DAtvarTe",
    text_dev              = "उपसर्गाच्छन्दसि धात्वर्थे",
    samagra_slp1          = "Candasi DAtvarTe upasargAt vatiH",
    samagra_dev           = "छन्दसि धात्वर्थे उपसर्गात् वतिः",
    padaccheda_dev        = "उपसर्गात् छन्दसि धातु-अर्थे",
    why_dev               = "(सूत्रम् 5.1.118) उपसर्गाच्छन्दसि धात्वर्थे।",
    anuvritti_from        = ('4.1.82',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
