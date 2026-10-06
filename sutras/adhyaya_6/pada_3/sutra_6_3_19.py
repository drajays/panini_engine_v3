"""
6.3.19  नेन्सिद्धबध्नातिषु  —  VIDHI

Padaccheda: न इन्-सिद्ध-बध्नातिषु

नेन्सिद्धबध्नातिषु (6.3.19)
Pāṭha: ashtadhyayi.com data.txt row i=63019 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_19_nensidDaba_19"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.19", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.19"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.19",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "nensidDabaDnAtizu",
    text_dev              = "नेन्सिद्धबध्नातिषु",
    samagra_slp1          = "alug uttarapade na in-sidDabaDnAtizu saptamyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे न इन्-सिद्धबध्नातिषु सप्तम्याः",
    padaccheda_dev        = "न इन्-सिद्ध-बध्नातिषु",
    why_dev               = "(सूत्रम् 6.3.19) नेन्सिद्धबध्नातिषु।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
