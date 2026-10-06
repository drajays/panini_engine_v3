"""
6.2.83  अन्त्यात् पूर्वं बह्वचः  —  VIDHI

Padaccheda: अन्त्यात् पूर्वम् बहु-अचः

अन्त्यात् पूर्वं बह्वचः (6.2.83)
Pāṭha: ashtadhyayi.com data.txt row i=62083 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_83_antyAt_83"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.83", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.83"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.83",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "antyAt pUrvaM bahvacaH",
    text_dev              = "अन्त्यात् पूर्वं बह्वचः",
    samagra_slp1          = "AdiH udAttaH antyAt pUrvam bahvacaH pUrvapadam je",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः उदात्तः अन्त्यात् पूर्वम् बह्वचः पूर्वपदम् जे",
    padaccheda_dev        = "अन्त्यात् पूर्वम् बहु-अचः",
    why_dev               = "(सूत्रम् 6.2.83) अन्त्यात् पूर्वं बह्वचः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
