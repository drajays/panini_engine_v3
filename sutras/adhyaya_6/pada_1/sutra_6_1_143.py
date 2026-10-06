"""
6.1.143  कुस्तुम्बुरूणि जातिः  —  VIDHI

Padaccheda: कुस्तुम्बुरूणि जातिः

कुस्तुम्बुरूणि जातिः (6.1.143)
Pāṭha: ashtadhyayi.com data.txt row i=61143 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_143_kustumburU_143"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.143", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.143"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.143",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "kustumburURi jAtiH",
    text_dev              = "कुस्तुम्बुरूणि जातिः",
    samagra_slp1          = "saMhitAyAm suwkAtpUrvaH kustumburURi jAtiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "संहितायाम् सुट्कात्पूर्वः कुस्तुम्बुरूणि जातिः",
    padaccheda_dev        = "कुस्तुम्बुरूणि जातिः",
    why_dev               = "(सूत्रम् 6.1.143) कुस्तुम्बुरूणि जातिः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
