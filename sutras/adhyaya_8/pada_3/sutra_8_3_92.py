"""
8.3.92  प्रष्ठोऽग्रगामिनि  —  VIDHI

Padaccheda: प्रष्ठः अग्रगामिनि

प्रष्ठोऽग्रगामिनि (8.3.92)
Pāṭha: ashtadhyayi.com data.txt row i=83092 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_92_prazWogra_92"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.92", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'prazWogragAmini',
    text_dev              = 'प्रष्ठोऽग्रगामिनि',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH prazWaH agragAmini saH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः प्रष्ठः अग्रगामिनि सः",
    padaccheda_dev        = "प्रष्ठः अग्रगामिनि",
    why_dev               = "(सूत्रम् 8.3.92) प्रष्ठोऽग्रगामिनि।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
