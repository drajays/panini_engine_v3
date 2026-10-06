"""
8.1.74  विभाषितं विशेषवचने बहुवचनम्  —  VIDHI

Padaccheda: विभाषितम् (सामान्यवचनम् ) विशेषवचने (बहुवचनम्)

विभाषितं विशेषवचने बहुवचनम् (8.1.74)
Pāṭha: ashtadhyayi.com data.txt row i=81074 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import tripadi_gate_eligible

_GATE_KEY: str = "8_1_74_viBAzitaM_74"


def cond(state: State) -> bool:
    return tripadi_gate_eligible(state, "8.1.74", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["sandhi_kind"]             = "8.1.74"
    return state


SUTRA = SutraRecord(
    sutra_id              = "8.1.74",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "viBAzitaM viSezavacane bahuvacanam",
    text_dev              = "विभाषितं विशेषवचने बहुवचनम्",
    samagra_slp1          = "padasya anudAttaM sarvamApAdAdO viBAzitam viSezavacane bahuvacanam Amantritam pUrvam avidyamAnavat Amantrite samAnADikaraRe",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "पदस्य अनुदात्तं सर्वमापादादौ विभाषितम् विशेषवचने बहुवचनम् आमन्त्रितम् पूर्वम् अविद्यमानवत् आमन्त्रिते समानाधिकरणे",
    padaccheda_dev        = "विभाषितम् (सामान्यवचनम् ) विशेषवचने (बहुवचनम्)",
    why_dev               = "(सूत्रम् 8.1.74) विभाषितं विशेषवचने बहुवचनम्।",
    anuvritti_from        = ('8.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
