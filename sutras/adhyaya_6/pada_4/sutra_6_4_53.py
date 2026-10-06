"""
6.4.53  जनिता मन्त्रे  —  VIDHI

Padaccheda: जनिता मन्त्रे

जनिता मन्त्रे (6.4.53)
Pāṭha: ashtadhyayi.com data.txt row i=64053 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_53_janitA_53"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.53", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.53"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.53",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "janitA mantre",
    text_dev              = "जनिता मन्त्रे",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke janitA mantre nalopaH lopaH ReH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके जनिता मन्त्रे नलोपः लोपः णेः",
    padaccheda_dev        = "जनिता मन्त्रे",
    why_dev               = "(सूत्रम् 6.4.53) जनिता मन्त्रे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
