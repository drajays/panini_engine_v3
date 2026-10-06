"""
6.3.121  इकः वहेऽपीलोः  —  VIDHI

Padaccheda: इकः वहे अपीलोः

इकः वहे अपीलोः (6.3.121)
Pāṭha: ashtadhyayi.com data.txt row i=63121 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import samhita_gate_eligible

_GATE_KEY: str = "6_3_121_ikaH_121"


def cond(state: State) -> bool:
    return samhita_gate_eligible(state, "6.3.121", gate_key=_GATE_KEY)


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["anga_kind"]             = "6.3.121"
    return state


SUTRA = SutraRecord(
    sutra_id              = "6.3.121",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = 'ikaH vahepIloH',
    text_dev              = 'इकः वहेऽपीलोः',
    samagra_slp1          = "uttarapade saMhitAyAm ikaH vahe apIloH dIrGaH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "उत्तरपदे संहितायाम् इकः वहे अपीलोः दीर्घः",
    padaccheda_dev        = "इकः वहे अपीलोः",
    why_dev               = "(सूत्रम् 6.3.121) इकः वहे अपीलोः।",
    anuvritti_from        = ('6.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
