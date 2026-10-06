"""
2.2.23  शेषो बहुव्रीहिः  —  VIDHI

Padaccheda: शेषः बहुव्रीहिः

Residual compounds are bahuvrihi.
Pāṭha: ashtadhyayi.com data.txt row i=22023 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State

_GATE_KEY: str = "2_2_23_sesa_bahuvrihi"


def cond(state: State) -> bool:
    if state.paribhasha_gates.get(_GATE_KEY) is True:
        return False
    return any("bahuvrIhi" in t.tags for t in state.terms)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["bahuvrihi_kind"]             = "2.2.23"
    return state


SUTRA = SutraRecord(
    sutra_id              = "2.2.23",
    sutra_type            = SutraType.SAMJNA,
    r1_form_identity_exempt = True,
    text_slp1             = "Sezo bahuvrIhiH",
    text_dev              = "शेषो बहुव्रीहिः",
    samagra_slp1          = "AkaqArAt ekA saMjYA prAkkaqArAtsamAsaH supsupA viBAzA SezaH bahuvrIhiH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "आकडारात् एका संज्ञा प्राक्कडारात्समासः सुप्सुपा विभाषा शेषः बहुव्रीहिः",
    padaccheda_dev        = "शेषः बहुव्रीहिः",
    why_dev               = "शेषः बहुव्रीहिः (२.२.२३)।",
    anuvritti_from        = ('2.2.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
