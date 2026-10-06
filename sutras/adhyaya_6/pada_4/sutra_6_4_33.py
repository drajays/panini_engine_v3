"""
6.4.33  भञ्जेश्च चिणि  —  VIDHI

Padaccheda: भञ्जेः च चिणि

भञ्जेश्च चिणि (6.4.33)
Pāṭha: ashtadhyayi.com data.txt row i=64033 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_33_BaYjeSca_33"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.33", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.33"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.33",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "BaYjeSca ciRi",
    text_dev              = "भञ्जेश्च चिणि",
    samagra_slp1          = "aNgasya asidDavadatrABAt BaYjeH ca ciRi nalopaH upaDAyAH na jAnta-naSAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भञ्जेः च चिणि नलोपः उपधायाः न जान्त-नशाम्",
    padaccheda_dev        = "भञ्जेः च चिणि",
    why_dev               = "(सूत्रम् 6.4.33) भञ्जेश्च चिणि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
