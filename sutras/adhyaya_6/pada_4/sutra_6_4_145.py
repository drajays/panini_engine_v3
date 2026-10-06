"""
6.4.145  अह्नष्टखोरेव  —  VIDHI

Padaccheda: अह्नः ट-खोः एव

अह्नष्टखोरेव (6.4.145)
Pāṭha: ashtadhyayi.com data.txt row i=64145 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_145_ahnazwaKor_145"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.145", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.145"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.145",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ahnazwaKoreva",
    text_dev              = "अह्नष्टखोरेव",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya ahnaH waKoH eva at-lopaH weH tadDite",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य अह्नः टखोः एव अत्-लोपः टेः तद्धिते",
    padaccheda_dev        = "अह्नः ट-खोः एव",
    why_dev               = "(सूत्रम् 6.4.145) अह्नष्टखोरेव।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
