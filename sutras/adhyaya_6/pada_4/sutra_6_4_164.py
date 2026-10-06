"""
6.4.164  इनण्यनपत्ये  —  VIDHI

Padaccheda: इन् अणि अन्-अपत्ये

इनण्यनपत्ये (6.4.164)
Pāṭha: ashtadhyayi.com data.txt row i=64164 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_164_inaRyanapa_164"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.164", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.164"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.164",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "inaRyanapatye",
    text_dev              = "इनण्यनपत्ये",
    samagra_slp1          = "aNgasya asidDavadatrABAt Basya in aRi anapatye prakftyA",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् भस्य इन् अणि अनपत्ये प्रकृत्या",
    padaccheda_dev        = "इन् अणि अन्-अपत्ये",
    why_dev               = "(सूत्रम् 6.4.164) इनण्यनपत्ये।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
