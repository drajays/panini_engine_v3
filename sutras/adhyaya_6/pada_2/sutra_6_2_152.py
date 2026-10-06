"""
6.2.152  सप्तम्याः पुण्यम्  —  VIDHI

Padaccheda: सप्तम्याः पुण्यम्

सप्तम्याः पुण्यम् (6.2.152)
Pāṭha: ashtadhyayi.com data.txt row i=62152 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_152_saptamyAH_152"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.152", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.152"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.152",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "saptamyAH puRyam",
    text_dev              = "सप्तम्याः पुण्यम्",
    samagra_slp1          = "uttarapadAdiH antaH saptamyAH puRyam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः सप्तम्याः पुण्यम्",
    padaccheda_dev        = "सप्तम्याः पुण्यम्",
    why_dev               = "(सूत्रम् 6.2.152) सप्तम्याः पुण्यम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
