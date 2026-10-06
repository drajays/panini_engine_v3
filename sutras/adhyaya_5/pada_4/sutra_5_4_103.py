"""
5.4.103  अनसन्तान्नपुंसकाच्छन्दसि  —  VIDHI

Padaccheda: अन्-अस्-अन्तात् नपुंसकात् छन्दसि

अनसन्तान्नपुंसकाच्छन्दसि (5.4.103)
Pāṭha: ashtadhyayi.com data.txt row i=54103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "5_4_103_anasantAnn_103"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("5.4.103", state, "5.4.68"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "5.4.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "5.4.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "anasantAnnapuMsakAcCandasi",
    text_dev              = "अनसन्तान्नपुंसकाच्छन्दसि",
    samagra_slp1          = "tatpuruzasya an-asantAt napuMsakAt Candasi wac",
    samagra_dev           = "तत्पुरुषस्य अन्-असन्तात् नपुंसकात्  छन्दसि टच्",
    padaccheda_dev        = "अन्-अस्-अन्तात् नपुंसकात् छन्दसि",
    why_dev               = "(सूत्रम् 5.4.103) अनसन्तान्नपुंसकाच्छन्दसि।",
    anuvritti_from        = ('5.4.68',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
