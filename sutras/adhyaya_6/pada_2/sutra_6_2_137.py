"""
6.2.137  प्रकृत्या भगालम्  —  VIDHI

Padaccheda: प्रकृत्या भगालम्

प्रकृत्या भगालम् (6.2.137)
Pāṭha: ashtadhyayi.com data.txt row i=62137 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_137_prakftyA_137"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.137", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "prakftyA BagAlam",
    text_dev              = "प्रकृत्या भगालम्",
    samagra_slp1          = "uttarapadAdiH prakftyA BagAlam tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः प्रकृत्या भगालम् तत्पुरुषे",
    padaccheda_dev        = "प्रकृत्या भगालम्",
    why_dev               = "(सूत्रम् 6.2.137) प्रकृत्या भगालम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
