"""
6.2.196  विभाषोत्पुच्छे  —  VIDHI

Padaccheda: विभाषा उत्पुच्छे

विभाषोत्पुच्छे (6.2.196)
Pāṭha: ashtadhyayi.com data.txt row i=62196 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_2_196_viBAzotpuc_196"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.2.196", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.2.196"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.2.196",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzotpucCe",
    text_dev              = "विभाषोत्पुच्छे",
    samagra_slp1          = "uttarapadAdiH antaH viBAzA utpucCe upasargAt tatpuruze",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदादिः अन्तः विभाषा उत्पुच्छे उपसर्गात् तत्पुरुषे",
    padaccheda_dev        = "विभाषा उत्पुच्छे",
    why_dev               = "(सूत्रम् 6.2.196) विभाषोत्पुच्छे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
