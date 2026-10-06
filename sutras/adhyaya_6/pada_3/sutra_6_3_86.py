"""
6.3.86  चरणे ब्रह्मचारिणि  —  VIDHI

Padaccheda: चरणे ब्रह्मचारिणि

चरणे ब्रह्मचारिणि (6.3.86)
Pāṭha: ashtadhyayi.com data.txt row i=63086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_86_caraRe_86"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.86", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "caraRe brahmacAriRi",
    text_dev              = "चरणे ब्रह्मचारिणि",
    samagra_slp1          = "uttarapade caraRe brahmacAriRi saH samAnasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे चरणे ब्रह्मचारिणि सः समानस्य",
    padaccheda_dev        = "चरणे ब्रह्मचारिणि",
    why_dev               = "(सूत्रम् 6.3.86) चरणे ब्रह्मचारिणि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
