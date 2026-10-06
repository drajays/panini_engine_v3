"""
6.3.88  विभाषोदरे  —  VIDHI

Padaccheda: विभाषा उदरे

विभाषोदरे (6.3.88)
Pāṭha: ashtadhyayi.com data.txt row i=63088 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_88_viBAzodare_88"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.88", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.88"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.88",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzodare",
    text_dev              = "विभाषोदरे",
    samagra_slp1          = "uttarapade viBAzA udare saH samAnasya",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे विभाषा उदरे सः समानस्य",
    padaccheda_dev        = "विभाषा उदरे",
    why_dev               = "(सूत्रम् 6.3.88) विभाषोदरे।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
