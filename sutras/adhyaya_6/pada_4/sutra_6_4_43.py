"""
6.4.43  ये विभाषा  —  VIDHI

Padaccheda: ये विभाषा

ये विभाषा (6.4.43)
Pāṭha: ashtadhyayi.com data.txt row i=64043 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_43_ye_43"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.43", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.43"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.43",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ye viBAzA",
    text_dev              = "ये विभाषा",
    samagra_slp1          = "aNgasya asidDavadatrABAt ye viBAzA nalopaH At jana-sana-KanAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् ये विभाषा नलोपः आत् जन-सन-खनाम्",
    padaccheda_dev        = "ये विभाषा",
    why_dev               = "(सूत्रम् 6.4.43) ये विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
