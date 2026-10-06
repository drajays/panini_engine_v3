"""
4.3.81  हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः  —  VIDHI

Padaccheda: हेतु-मनुष्येभ्यः अन्यतरस्याम् रूप्यः

हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः (4.3.81)
Pāṭha: ashtadhyayi.com data.txt row i=43081 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State

_GATE_KEY: str = "4_3_81_hetumanuzy_81"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    if not adhikara_in_effect("4.3.81", state, "4.1.76"):
        return False
    if not any("prātipadika" in t.tags or "anga" in t.tags for t in state.terms):
        return False
    if any("taddhita" in t.tags and "pratyaya" in t.tags for t in state.terms):
        return False
    return True


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["taddhita_kind"]             = "4.3.81"
    return state


SUTRA = SutraRecord(
    sutra_id              = "4.3.81",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'hetumanuzyeByonyatarasyAM rUpyaH',
    text_dev              = 'हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः',
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca NyApprAtipadikAt tadDitAH prAgdIvyatoR samarTAnAM praTamAdvA hetu-manuzyeByaH anyatarasyAm rUpyaH AgataH tata",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च ङ्याप्प्रातिपदिकात् तद्धिताः प्राग्दीव्यतोऽण् समर्थानां प्रथमाद्वा हेतु-मनुष्येभ्यः अन्यतरस्याम् रूप्यः आगतः तत",
    padaccheda_dev        = "हेतु-मनुष्येभ्यः अन्यतरस्याम् रूप्यः",
    why_dev               = "(सूत्रम् 4.3.81) हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः।",
    anuvritti_from        = ('4.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
