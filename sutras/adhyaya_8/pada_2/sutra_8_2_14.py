"""
8.2.14  राजन्वान् सौराज्ये  —  VIDHI

Padaccheda: राजन्वान् सौराज्ये

राजन्वान् सौराज्ये (8.2.14)
Pāṭha: ashtadhyayi.com data.txt row i=82014 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_2_14_rAjanvAn_14"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.2.14", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.2.14"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.2.14",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "rAjanvAn sOrAjye",
    text_dev              = "राजन्वान् सौराज्ये",
    samagra_slp1          = "padasya pUrvatrAsidDam rAjanvAn sOrAjye vaH matoH saMjYAyAm",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य पूर्वत्रासिद्धम् राजन्वान् सौराज्ये वः मतोः संज्ञायाम्",
    padaccheda_dev        = "राजन्वान् सौराज्ये",
    why_dev               = "(सूत्रम् 8.2.14) राजन्वान् सौराज्ये।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
