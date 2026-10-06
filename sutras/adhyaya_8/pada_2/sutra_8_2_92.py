"""
8.2.92  अग्नीत्प्रेषणे परस्य च  —  VIDHI

Padaccheda: अग्नीत्प्रेषणे परस्य च

अग्नीत्प्रेषणे परस्य च (8.2.92)
Pāṭha: ashtadhyayi.com data.txt row i=82092 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_92_agnItpreza_92"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.92", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.92"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.92",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "agnItprezaRe parasya ca",
    text_dev              = "अग्नीत्प्रेषणे परस्य च",
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH agnItprezaRe parasya ca yajYakarmaRi AdeH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः अग्नीत्प्रेषणे परस्य च यज्ञकर्मणि आदेः",
    padaccheda_dev        = "अग्नीत्प्रेषणे परस्य च",
    why_dev               = "(सूत्रम् 8.2.92) अग्नीत्प्रेषणे परस्य च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
