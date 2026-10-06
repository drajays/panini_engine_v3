"""
3.2.137  णेश्छन्दसि  —  VIDHI

Padaccheda: णेः छन्दसि

krt-suffix rule: णेश्छन्दसि (137)
Pāṭha: ashtadhyayi.com data.txt row i=32137 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_137_ReSCandasi_137"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.137", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.137"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.137",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "ReSCandasi",
    text_dev              = "णेश्छन्दसि",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH vartamAne A kvestacCIlatadDarmatatsADukArizu ReH Candasi kft izRuc",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः वर्तमाने आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु णेः छन्दसि कृत् इष्णुच्",
    padaccheda_dev        = "णेः छन्दसि",
    why_dev               = "धातोः कृत्-प्रत्ययः [णेश्छन्दसि] विहितः (३.२.137)।",
    anuvritti_from        = ('3.1.1', '3.2.78'),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
