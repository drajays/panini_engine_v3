"""
6.3.120  शरादीनां च  —  VIDHI

Padaccheda: शर-आदीनाम् च

शरादीनां च (6.3.120)
Pāṭha: ashtadhyayi.com data.txt row i=63120 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_120_SarAdInAM_120"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.120", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.120"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.120",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SarAdInAM ca",
    text_dev              = "शरादीनां च",
    samagra_slp1          = "uttarapade saMhitAyAm SarAdInAm ca dIrGaH saMjYAyAm matO",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् शरादीनाम् च दीर्घः संज्ञायाम् मतौ",
    padaccheda_dev        = "शर-आदीनाम् च",
    why_dev               = "(सूत्रम् 6.3.120) शरादीनां च।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
