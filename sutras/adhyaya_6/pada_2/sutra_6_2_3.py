"""
6.2.3  वर्णो वर्णेष्वनेते  —  VIDHI

Padaccheda: वर्णः वर्णेषु अनेते

वर्णः वर्णेष्वनेते (6.2.3)
Pāṭha: ashtadhyayi.com data.txt row i=62003 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_3_varRaH_3"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.3", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.3"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.3",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'varRo varRezvanete',
    text_dev              = 'वर्णो वर्णेष्वनेते',
    samagra_slp1          = "varRaH varRezu anete prakftyA pUrvapadam tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "वर्णः वर्णेषु अनेते प्रकृत्या पूर्वपदम् तत्पुरुषे",
    padaccheda_dev        = "वर्णः वर्णेषु अनेते",
    why_dev               = "(सूत्रम् 6.2.3) वर्णः वर्णेष्वनेते।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
