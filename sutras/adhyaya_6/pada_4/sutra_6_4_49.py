"""
6.4.49  यस्य हलः  —  VIDHI

Padaccheda: यस्य हलः

यस्य हलः (6.4.49)
Pāṭha: ashtadhyayi.com data.txt row i=64049 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_49_yasya_49"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.49", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.49"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.49",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "yasya halaH",
    text_dev              = "यस्य हलः",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke yasya halaH nalopaH lopaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके यस्य हलः नलोपः लोपः",
    padaccheda_dev        = "यस्य हलः",
    why_dev               = "(सूत्रम् 6.4.49) यस्य हलः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
