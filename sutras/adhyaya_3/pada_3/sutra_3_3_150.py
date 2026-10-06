"""
3.3.150  चित्रीकरणे च  —  VIDHI

Padaccheda: चित्रीकरणे च

krt-suffix rule: चित्रीकरणे च
Pāṭha: ashtadhyayi.com data.txt row i=33150 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_3_150_citrIkaraR_150"


def cond(state: State) -> bool:
    return krt_insertion_eligible(state, "3.3.150", gate_key=_GATE_KEY, adhikara_id="3.1.1")


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.3.150"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.3.150",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "citrIkaraRe ca",
    text_dev              = "चित्रीकरणे च",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH citrIkaraRe ca kft utApyoH liN yacca-yatrayoH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः चित्रीकरणे च कृत् उताप्योः लिङ् यच्च-यत्रयोः",
    padaccheda_dev        = "चित्रीकरणे च",
    why_dev               = "धातोः प्रत्ययः (३.3.150)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
