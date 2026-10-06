"""
6.1.209  जुष्टार्पिते च छन्दसि  —  VIDHI

Padaccheda: जुष्ट-अर्पिते च छन्दसि

जुष्टार्पिते च छन्दसि (6.1.209)
Pāṭha: ashtadhyayi.com data.txt row i=61209 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_209_juzwArpite_209"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.209", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.209"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.209",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "juzwArpite ca Candasi",
    text_dev              = "जुष्टार्पिते च छन्दसि",
    samagra_slp1          = "juzwa-arpite ca Candasi udAttaH AdiH viBAzA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "जुष्ट-अर्पिते च छन्दसि उदात्तः आदिः विभाषा",
    padaccheda_dev        = "जुष्ट-अर्पिते च छन्दसि",
    why_dev               = "(सूत्रम् 6.1.209) जुष्टार्पिते च छन्दसि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
