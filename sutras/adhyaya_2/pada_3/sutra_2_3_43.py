"""
2.3.43  साधुनिपुणाभ्यामर्चायां सप्तम्यप्रतेः  —  VIDHI

Padaccheda: साधु-निपुणाभ्याम् अर्चायाम् सप्तमी अ-प्रतेः

sadhu and nipuna in worship context take saptami.
Pāṭha: ashtadhyayi.com data.txt row i=23043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.subanta_eligibility import karaka_gate_eligible

_GATE_KEY: str = "2_3_43_sadhu_nipuna"


def cond(state: State) -> bool:
    return karaka_gate_eligible(state, _GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["vibhakti_kind"]             = "2.3.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.3.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'sADunipuRAByAmarcAyAM saptamyaprateH',
    text_dev              = 'साधुनिपुणाभ्यामर्चायां सप्तम्यप्रतेः',
    samagra_slp1          = "anaBihite sADu-nipuRAByAm arcAyAm saptamI aprateH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अनभिहिते साधु-निपुणाभ्याम् अर्चायाम् सप्तमी अप्रतेः",
    padaccheda_dev        = "साधु-निपुणाभ्याम् अर्चायाम् सप्तमी अ-प्रतेः",
    why_dev               = "साधु-निपुणाभ्याम् अर्चायाम् सप्तमी (२.३.४३)।",
    anuvritti_from        = ('2.3.36',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
