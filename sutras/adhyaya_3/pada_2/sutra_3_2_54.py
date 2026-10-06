"""
3.2.54  शक्तौ हस्तिकपाटयोः  —  VIDHI

Padaccheda: शक्तौ हस्ति-कपाटयोः

krt-suffix rule: शक्तौ हस्तिकपाटयोः (54)
Pāṭha: ashtadhyayi.com data.txt row i=32054 (Art. 14).
"""
from __future__ import annotations

from engine       import SutraType, SutraRecord, register_sutra
from engine.state import State
from engine.krt_eligibility import krt_insertion_eligible

_GATE_KEY: str = "3_2_54_SaktO_54"


def cond(state: State) -> bool:
    if not krt_insertion_eligible(state, "3.2.54", gate_key=_GATE_KEY, adhikara_id="3.1.1"):
        return False
    return not any(
        "krt" in t.tags and "pratyaya" in t.tags for t in state.terms
    )


def act(state: State) -> State:
    state.paribhasha_gates[_GATE_KEY] = True
    state.samjna_registry[_GATE_KEY]  = True
    state.meta["krt_kind"] = "3.2.54"
    return state


SUTRA = SutraRecord(
    sutra_id              = "3.2.54",
    sutra_type            = SutraType.VIDHI,
    r1_form_identity_exempt = True,
    text_slp1             = "SaktO hastikapAwayoH",
    text_dev              = "शक्तौ हस्तिकपाटयोः",
    samagra_slp1          = "pratyayaH paraSca AdyudAttaSca DAtoH SaktO hasti-kapAwayoH kft karmaRi anupasarge supi hanaH wak",  # samagra composed: adhikāra + padas + anuvṛtti (ashtadhyayi.com); vipariṇāma unchecked
    samagra_dev           = "प्रत्ययः परश्च आद्युदात्तश्च धातोः शक्तौ हस्ति-कपाटयोः कृत् कर्मणि अनुपसर्गे सुपि हनः टक्",
    padaccheda_dev        = "शक्तौ हस्ति-कपाटयोः",
    why_dev               = "धातोः कृत्-प्रत्ययः [शक्तौ हस्तिकपाटयोः] विहितः (३.२.54)।",
    anuvritti_from        = ('3.1.1',),
    cond                  = cond,
    act                   = act,
)

register_sutra(SUTRA)
