"""
6.4.121  थलि च सेटि  —  VIDHI

Padaccheda: थलि च सेटि

थलि च सेटि (6.4.121)
Pāṭha: ashtadhyayi.com data.txt row i=64121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_121_Tali_121"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.121", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "Tali ca sewi",
    text_dev              = "थलि च सेटि",
    samagra_slp1          = "aNgasya asidDavadatrABAt Tali ca sewi et hO aByAsalopaH ekahalmaDye anAdeSAdeH liwi ataH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य असिद्धवदत्राभात् थलि च सेटि एत् हौ अभ्यासलोपः एकहल्मध्ये अनादेशादेः लिटि अतः",
    padaccheda_dev        = "थलि च सेटि",
    why_dev               = "(सूत्रम् 6.4.121) थलि च सेटि।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
