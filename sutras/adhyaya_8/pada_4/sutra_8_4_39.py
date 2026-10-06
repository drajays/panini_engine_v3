"""
8.4.39  क्षुभ्नाऽऽदिषु च  —  VIDHI

Padaccheda: क्षुभ्ना-आदिषु च

क्षुभ्नाऽऽदिषु च (8.4.39)
Pāṭha: ashtadhyayi.com data.txt row i=84039 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_39_kzuBnAdi_39"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.39", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.39"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.39",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'kzuBnAdizu ca',
    text_dev              = 'क्षुभ्नाऽऽदिषु च',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm kzuBnA-Adizu ca razAByAm na",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् क्षुभ्ना-आदिषु च रषाभ्याम् न",
    padaccheda_dev        = "क्षुभ्ना-आदिषु च",
    why_dev               = "(सूत्रम् 8.4.39) क्षुभ्नाऽऽदिषु च।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
