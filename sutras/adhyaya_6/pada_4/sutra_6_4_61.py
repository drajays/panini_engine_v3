"""
6.4.61  वाक्रोशदैन्ययोः  —  VIDHI

Padaccheda: वा आक्रोश-दैन्ययोः

वाऽऽक्रोशदैन्ययोः (6.4.61)
Pāṭha: ashtadhyayi.com data.txt row i=64061 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_61_vAkroSad_61"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.61", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.61"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.61",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'vAkroSadEnyayoH',
    text_dev              = 'वाक्रोशदैन्ययोः',
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke vA AkroSa-dEnyayoH dIrGaH kziyaH nizWAyAm a-Ryat-arTe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके वा आक्रोश-दैन्ययोः दीर्घः क्षियः निष्ठायाम् अ-ण्यत्-अर्थे",
    padaccheda_dev        = "वा आक्रोश-दैन्ययोः",
    why_dev               = "(सूत्रम् 6.4.61) वाऽऽक्रोशदैन्ययोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
