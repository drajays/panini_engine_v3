"""
3.2.86  कर्मणि हनः  —  VIDHI

Padaccheda: कर्मणि हनः

krt-suffix rule: कर्मणि हनः (86)
Pāṭha: ashtadhyayi.com data.txt row i=32086 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_86_karmaRi_86"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.86", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.86"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.86",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "karmaRi hanaH",
    text_dev              = "कर्मणि हनः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH BUte karmaRi hanaH kft RiniH",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः भूते कर्मणि हनः कृत् णिनिः",
    padaccheda_dev        = "कर्मणि हनः",
    why_dev               = "धातोः कृत्-प्रत्ययः [कर्मणि हनः] विहितः (३.२.86)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
