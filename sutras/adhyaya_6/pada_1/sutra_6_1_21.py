"""
6.1.21  चायः की  —  VIDHI

Padaccheda: चायः की (लुप्तप्रथमान्तनिर्देशः)

चायः की (6.1.21)
Pāṭha: ashtadhyayi.com data.txt row i=61021 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_21_cAyaH_21"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.21", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.21"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.21",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "cAyaH kI",
    text_dev              = "चायः की",
    samagra_slp1          = "cAyaH kI samprasAraRam yaNi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "चायः की सम्प्रसारणम् यङि",
    padaccheda_dev        = "चायः की (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "(सूत्रम् 6.1.21) चायः की।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
