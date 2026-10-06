"""
6.1.28  प्यायः पी  —  VIDHI

Padaccheda: प्यायः पी (लुप्तप्रथमान्तनिर्देशः)

प्यायः पी (6.1.28)
Pāṭha: ashtadhyayi.com data.txt row i=61028 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_28_pyAyaH_28"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.28", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.28"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.28",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "pyAyaH pI",
    text_dev              = "प्यायः पी",
    samagra_slp1          = "pyAyaH pI samprasAraRam nizWAyAm viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्यायः पी सम्प्रसारणम् निष्ठायाम् विभाषा",
    padaccheda_dev        = "प्यायः पी (लुप्तप्रथमान्तनिर्देशः)",
    why_dev               = "(सूत्रम् 6.1.28) प्यायः पी।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
