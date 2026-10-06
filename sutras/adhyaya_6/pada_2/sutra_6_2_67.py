"""
6.2.67  विभाषाऽध्यक्षे  —  VIDHI

Padaccheda: विभाषा अध्यक्षे

विभाषाऽध्यक्षे (6.2.67)
Pāṭha: ashtadhyayi.com data.txt row i=62067 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_67_viBAzADya_67"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.67", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.67"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.67",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'viBAzADyakze',
    text_dev              = 'विभाषाऽध्यक्षे',
    samagra_slp1          = "AdiH udAttaH viBAzA aDyakze pUrvapadam",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आदिः उदात्तः विभाषा अध्यक्षे पूर्वपदम्",
    padaccheda_dev        = "विभाषा अध्यक्षे",
    why_dev               = "(सूत्रम् 6.2.67) विभाषाऽध्यक्षे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
