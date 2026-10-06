"""
6.4.69  न ल्यपि  —  VIDHI

Padaccheda: न ल्यपि

न ल्यपि (6.4.69)
Pāṭha: ashtadhyayi.com data.txt row i=64069 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_69_na_69"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.69", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.69"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.69",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na lyapi",
    text_dev              = "न ल्यपि",
    samagra_slp1          = "aNgasya asidDavadatrABAt ArDaDAtuke na lyapi AtaH Gu-mA-sTA-gA-pA-jahAti-sAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् आर्धधातुके न ल्यपि आतः घु-मा-स्था-गा-पा-जहाति-साम्",
    padaccheda_dev        = "न ल्यपि",
    why_dev               = "(सूत्रम् 6.4.69) न ल्यपि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
