"""
6.3.4  मनसः संज्ञायाम्  —  VIDHI

Padaccheda: मनसः संज्ञायाम्

मनसः संज्ञायाम् (6.3.4)
Pāṭha: ashtadhyayi.com data.txt row i=63004 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_4_manasaH_4"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.4", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.4"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.4",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "manasaH saMjYAyAm",
    text_dev              = "मनसः संज्ञायाम्",
    samagra_slp1          = "alug uttarapade manasaH saMjYAyAm tftIyAyAH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अलुग् उत्तरपदे मनसः संज्ञायाम् तृतीयायाः",
    padaccheda_dev        = "मनसः संज्ञायाम्",
    why_dev               = "(सूत्रम् 6.3.4) मनसः संज्ञायाम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
