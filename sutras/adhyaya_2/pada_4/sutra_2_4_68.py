"""
2.4.68  तिककितवादिभ्यो द्वन्द्वे  —  VIDHI

Padaccheda: तिक-कितव-आदिभ्यः द्वन्द्वे

tika, kitava etc. in dvandva compound.
Pāṭha: ashtadhyayi.com data.txt row i=24068 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_4_68_tika_kitava_dvandva"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("dvandva_samasa" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["dvandva_kind"]             = "2.4.68"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.4.68",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'tikakitavAdiByo dvandve',
    text_dev              = 'तिककितवादिभ्यो द्वन्द्वे',
    samagra_slp1          = "tikakitava-AdiByaH dvandve luk bahuzu tena eva astriyAm gotre",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "तिककितव-आदिभ्यः द्वन्द्वे लुक् बहुषु तेन एव अस्त्रियाम् गोत्रे",
    padaccheda_dev        = "तिक-कितव-आदिभ्यः द्वन्द्वे",
    why_dev               = "तिक-कितव-आदिभ्यः द्वन्द्वे (२.४.६८)।",
    anuvritti_from        = ('2.4.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
