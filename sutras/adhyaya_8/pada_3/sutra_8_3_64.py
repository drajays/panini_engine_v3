"""
8.3.64  स्थाऽऽदिष्वभ्यासेन चाभ्यासस्य  —  VIDHI

Padaccheda: स्था-आदिषु अभ्यासेन च अभ्यासस्य

स्थाऽऽदिष्वभ्यासेन चाभ्यासय (8.3.64)
Pāṭha: ashtadhyayi.com data.txt row i=83064 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_3_64_sTAdizva_64"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.3.64", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.3.64"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.3.64",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'sTAdizvaByAsena cAByAsasya',
    text_dev              = 'स्थाऽऽदिष्वभ्यासेन चाभ्यासस्य',
    samagra_slp1          = "pUrvatrAsidDam saMhitAyAm apadAntasya mUrDanyaH iRkoH sTAdizu aByAsena ca aByAsasya saH aqvyavAye api",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पूर्वत्रासिद्धम् संहितायाम् अपदान्तस्य मूर्धन्यः इण्कोः स्थाऽऽदिषु अभ्यासेन च अभ्यासस्य सः अड्व्यवाये अपि",
    padaccheda_dev        = "स्था-आदिषु अभ्यासेन च अभ्यासस्य",
    why_dev               = "(सूत्रम् 8.3.64) स्थाऽऽदिष्वभ्यासेन चाभ्यासय।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
