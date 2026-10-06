"""
8.2.103  स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु  —  VIDHI

Padaccheda: स्वरितम् आम्रेडिते असूया-सम्मति-कोप-कुत्सनेषु

स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु (8.2.103)
Pāṭha: ashtadhyayi.com data.txt row i=82103 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_103_svaritamAm_103"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.103", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.103"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.103",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'svaritamAmreqitesUyAsammatikopakutsanezu',
    text_dev              = 'स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु',
    samagra_slp1          = "padasya pUrvatrAsidDam vAkyasya weH plutaH udAttaH svaritam Amreqite asUyAsammatikopakutsanezu",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् वाक्यस्य टेः प्लुतः उदात्तः स्वरितम् आम्रेडिते असूयासम्मतिकोपकुत्सनेषु",
    padaccheda_dev        = "स्वरितम् आम्रेडिते असूया-सम्मति-कोप-कुत्सनेषु",
    why_dev               = "(सूत्रम् 8.2.103) स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
