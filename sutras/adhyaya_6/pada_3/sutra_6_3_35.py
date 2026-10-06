"""
6.3.35  तसिलादिष्वाकृत्वसुचः  —  VIDHI

Padaccheda: तसिलादिषु आ कृत्वसुचः

तसिलादिषु आकृत्वसुचः (6.3.35)
Pāṭha: ashtadhyayi.com data.txt row i=63035 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_35_tasilAdizu_35"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.35", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.35"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.35",
    sutra_type            = SutraType.ATIDESHA,
    r1_form_identity_exempt = True,
    text_slp1             = 'tasilAdizvAkftvasucaH',
    text_dev              = 'तसिलादिष्वाकृत्वसुचः',
    samagra_slp1          = "uttarapade tasilAdizu A kftvasucaH striyAH puMvat anUN BAzitapu~skAd",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे तसिलादिषु आ कृत्वसुचः स्त्रियाः पुंवत् अनूङ् भाषितपुँस्काद्",
    padaccheda_dev        = "तसिलादिषु आ कृत्वसुचः",
    why_dev               = "(सूत्रम् 6.3.35) तसिलादिषु आकृत्वसुचः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
