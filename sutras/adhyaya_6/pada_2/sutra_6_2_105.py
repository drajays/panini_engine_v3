"""
6.2.105  उत्तरपदवृद्धौ सर्वं च  —  VIDHI

Padaccheda: उत्तरपद-वृद्धौ सर्वम् च

उत्तरपदवृद्धौ सर्वं च (6.2.105)
Pāṭha: ashtadhyayi.com data.txt row i=62105 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_105_uttarapada_105"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.105", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.105"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.105",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "uttarapadavfdDO sarvaM ca",
    text_dev              = "उत्तरपदवृद्धौ सर्वं च",
    samagra_slp1          = "udAttaH antaH uttarapadavfdDO sarvam ca pUrvapadam dikSabdAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उदात्तः अन्तः उत्तरपदवृद्धौ सर्वम् च पूर्वपदम् दिक्शब्दाः",
    padaccheda_dev        = "उत्तरपद-वृद्धौ सर्वम् च",
    why_dev               = "(सूत्रम् 6.2.105) उत्तरपदवृद्धौ सर्वं च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
