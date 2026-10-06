"""
8.4.34  न भाभूपूकमिगमिप्यायीवेपाम्  —  VIDHI

Padaccheda: न भा-भू-पू-कमि-गमि-प्यायी-वेपाम्

न भाभूपूकमिगमिप्यायीवेपाम् (8.4.34)
Pāṭha: ashtadhyayi.com data.txt row i=84034 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_4_34_na_34"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.4.34", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.4.34"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.4.34",
    sutra_type            = SutraType.PRATISHEDHA,
    r1_form_identity_exempt = True,
    text_slp1             = "na BABUpUkamigamipyAyIvepAm",
    text_dev              = "न भाभूपूकमिगमिप्यायीवेपाम्",
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm na BA-BU-pU-kami-gami-pyAyI-vepAm razAByAm upasargAt kfti",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् न भा-भू-पू-कमि-गमि-प्यायी-वेपाम् रषाभ्याम् उपसर्गात् कृति",
    padaccheda_dev        = "न भा-भू-पू-कमि-गमि-प्यायी-वेपाम्",
    why_dev               = "(सूत्रम् 8.4.34) न भाभूपूकमिगमिप्यायीवेपाम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
