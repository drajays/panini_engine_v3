"""
6.4.124  वा जॄभ्रमुत्रसाम्  —  VIDHI

Padaccheda: वा जॄ-भ्रमु-त्रसाम्

वा जॄभ्रमुत्रसाम् (6.4.124)
Pāṭha: ashtadhyayi.com data.txt row i=64124 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_124_vA_124"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.124", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.124"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.124",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "vA jFBramutrasAm",
    text_dev              = "वा जॄभ्रमुत्रसाम्",
    samagra_slp1          = "aNgasya asidDavadatrABAt vA jF-Bramu-trasAm kNiti aByAsalopaH ataH Tali sewi",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् वा जॄ-भ्रमु-त्रसाम् क्ङिति अभ्यासलोपः अतः थलि सेटि",
    padaccheda_dev        = "वा जॄ-भ्रमु-त्रसाम्",
    why_dev               = "(सूत्रम् 6.4.124) वा जॄभ्रमुत्रसाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
