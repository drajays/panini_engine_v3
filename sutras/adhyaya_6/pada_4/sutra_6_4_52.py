"""
6.4.52  निष्ठायां सेटि  —  VIDHI

Padaccheda: निष्ठायाम् सेटि

निष्ठायां सेटि (6.4.52)
Pāṭha: ashtadhyayi.com data.txt row i=64052 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_52_nizWAyAM_52"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.52", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.52"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.52",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "nizWAyAM sewi",
    text_dev              = "निष्ठायां सेटि",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke nizWAyAm sewi nalopaH lopaH ReH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके निष्ठायाम् सेटि नलोपः लोपः णेः",
    padaccheda_dev        = "निष्ठायाम् सेटि",
    why_dev               = "(सूत्रम् 6.4.52) निष्ठायां सेटि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
