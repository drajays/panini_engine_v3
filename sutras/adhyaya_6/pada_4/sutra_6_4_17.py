"""
6.4.17  तनोतेर्विभाषा  —  VIDHI

Padaccheda: तनोतेः विभाषा

तनोतेर्विभाषा (6.4.17)
Pāṭha: ashtadhyayi.com data.txt row i=64017 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.gates import adhikara_in_effect
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_4_17_tanoterviB_17"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.4.17", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.4.17"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.4.17",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "tanoterviBAzA",
    text_dev              = "तनोतेर्विभाषा",
    samagra_slp1          = "aNgasya tanoteH viBAzA dIrGaH na upaDAyAH kvi-JaloH kNiti sani",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "अङ्गस्य तनोतेः विभाषा दीर्घः न उपधायाः क्वि-झलोः क्ङिति सनि",
    padaccheda_dev        = "तनोतेः विभाषा",
    why_dev               = "(सूत्रम् 6.4.17) तनोतेर्विभाषा।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
