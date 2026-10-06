"""
6.3.37  न कोपधायाः  —  VIDHI

Padaccheda: न कउपधायाः

न कोपधायाः (6.3.37)
Pāṭha: ashtadhyayi.com data.txt row i=63037 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_37_na_37"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.37", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.37"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.37",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na kopaDAyAH",
    text_dev              = "न कोपधायाः",
    samagra_slp1          = "uttarapade na kopaDAyAH striyAH puMvat anUN BAzitapu~skAd",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे न कोपधायाः स्त्रियाः पुंवत् अनूङ् भाषितपुँस्काद्",
    padaccheda_dev        = "न कउपधायाः",
    why_dev               = "(सूत्रम् 6.3.37) न कोपधायाः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
