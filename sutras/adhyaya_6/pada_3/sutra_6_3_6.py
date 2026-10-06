"""
6.3.6  आत्मनश्च पूरणे  —  VIDHI

Padaccheda: आत्मनः च पूरणे

आत्मनश्च पूरणे (6.3.6)
Pāṭha: ashtadhyayi.com data.txt row i=63006 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_6_AtmanaSca_6"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.6", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.6"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.6",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "AtmanaSca pUraRe",
    text_dev              = "आत्मनश्च पूरणे",
    samagra_slp1          = "alug uttarapade AtmanaH ca pUraRe tftIyAyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे आत्मनः च पूरणे तृतीयायाः",
    padaccheda_dev        = "आत्मनः च पूरणे",
    why_dev               = "(सूत्रम् 6.3.6) आत्मनश्च पूरणे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
