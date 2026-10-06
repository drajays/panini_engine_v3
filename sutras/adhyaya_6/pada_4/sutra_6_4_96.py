"""
6.4.96  छादेर्घेऽद्व्युपसर्गस्य  —  VIDHI

Padaccheda: छादेः घे अ-द्वि-उपसर्गस्य

छादेर्घेऽद्व्युपसर्गस्य (6.4.96)
Pāṭha: ashtadhyayi.com data.txt row i=64096 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_96_CAderGedv_96"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.96", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.96"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.96",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'CAderGedvyupasargasya',
    text_dev              = 'छादेर्घेऽद्व्युपसर्गस्य',
    samagra_slp1          = "aNgasya asidDavadatrABAt CAdeH Ge a-dvyupasargasya aci upaDAyAH hrasvaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् छादेः घे अ-द्व्युपसर्गस्य अचि उपधायाः ह्रस्वः",
    padaccheda_dev        = "छादेः घे अ-द्वि-उपसर्गस्य",
    why_dev               = "(सूत्रम् 6.4.96) छादेर्घेऽद्व्युपसर्गस्य।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
