"""
6.4.126  न शसददवादिगुणानाम्  —  VIDHI

Padaccheda: न शस-दद-व-आदि-गुणानाम्

न शसददवादिगुणानाम् (6.4.126)
Pāṭha: ashtadhyayi.com data.txt row i=64126 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_126_na_126"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.126", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.126"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.126",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na SasadadavAdiguRAnAm",
    text_dev              = "न शसददवादिगुणानाम्",
    samagra_slp1          = "aNgasya asidDavadatrABAt na Sa-sadada-vAdi-guRAnAm kNiti aByAsalopaH ataH Tali sewi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् न श-सदद-वादि-गुणानाम् क्ङिति अभ्यासलोपः अतः थलि सेटि",
    padaccheda_dev        = "न शस-दद-व-आदि-गुणानाम्",
    why_dev               = "(सूत्रम् 6.4.126) न शसददवादिगुणानाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
