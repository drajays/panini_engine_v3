"""
6.3.40  स्वाङ्गाच्चेतोऽमानिनि  —  VIDHI

Padaccheda: स्वाङ्गात् च ईतः अमानिनि

स्वाङ्गाच्चेतोऽमानिनि (6.3.40)
Pāṭha: ashtadhyayi.com data.txt row i=63040 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_40_svANgAccet_40"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.40", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.40"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.40",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'svANgAccetomAnini',
    text_dev              = 'स्वाङ्गाच्चेतोऽमानिनि',
    samagra_slp1          = "uttarapade svANgAt ca ItaH amAnini striyAH puMvat anUN BAzitapu~skAd na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे स्वाङ्गात् च ईतः अमानिनि स्त्रियाः पुंवत् अनूङ् भाषितपुँस्काद् न",
    padaccheda_dev        = "स्वाङ्गात् च ईतः अमानिनि",
    why_dev               = "(सूत्रम् 6.3.40) स्वाङ्गाच्चेतोऽमानिनि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
