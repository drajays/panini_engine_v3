"""
6.4.34  शास इदङ्हलोः  —  VIDHI

Padaccheda: शासः इत् अङ्-हलोः

शास इदङ्हलोः (6.4.34)
Pāṭha: ashtadhyayi.com data.txt row i=64034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_34_SAsa_34"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.34", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.34",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SAsa idaNhaloH",
    text_dev              = "शास इदङ्हलोः",
    samagra_slp1          = "aNgasya asidDavadatrABAt SAsaH it aN-haloH nalopaH upaDAyAH kNiti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् शासः इत् अङ्-हलोः नलोपः उपधायाः क्ङिति",
    padaccheda_dev        = "शासः इत् अङ्-हलोः",
    why_dev               = "(सूत्रम् 6.4.34) शास इदङ्हलोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
