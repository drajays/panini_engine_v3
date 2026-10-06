"""
6.1.187  आदिः सिचोऽन्यतरस्याम्  —  VIDHI

Padaccheda: आदिः सिचः अन्यतरस्याम्

आदिः सिचोऽन्यतरस्याम् (6.1.187)
Pāṭha: ashtadhyayi.com data.txt row i=61187 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_1_187_AdiH_187"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.1.187", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.1.187"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.1.187",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'AdiH siconyatarasyAm',
    text_dev              = 'आदिः सिचोऽन्यतरस्याम्',
    samagra_slp1          = "AdiH sicaH anyatarasyAm udAttaH nAm la-sArvaDAtukam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः सिचः अन्यतरस्याम् उदात्तः नाम् ल-सार्वधातुकम्",
    padaccheda_dev        = "आदिः सिचः अन्यतरस्याम्",
    why_dev               = "(सूत्रम् 6.1.187) आदिः सिचोऽन्यतरस्याम्।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
